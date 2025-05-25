import chromadb
from chromadb.utils import embedding_functions
import os
from utils import load_data

# Model adi
MODEL_NAME = "sentence-transformers/all-MiniLM-L12-v2"

# ChromaDB ayarlari
CHROMA_DATA_PATH = os.path.join(os.path.dirname(__file__), '..', 'chroma_db_data')
COLLECTION_NAME = "soru_cevap_collection"

# Sentence Transformer embedding fonksiyonunu baslat
sentence_transformer_ef = embedding_functions.SentenceTransformerEmbeddingFunction(model_name=MODEL_NAME)

# ChromaDB istemcisini baslat (kalici depolama)
try:
    client = chromadb.PersistentClient(path=CHROMA_DATA_PATH)
except Exception as e:
    print(f"Chromadb PersistentClient baslatilirken hata: {e}")
    print("EphemeralClient kullanilacak (veriler gecici olacak).")
    client = chromadb.EphemeralClient()


def get_or_create_collection(client: chromadb.Client, name: str, embedding_function: callable):
    try:
        collection = client.get_collection(name=name, embedding_function=embedding_function)
        print(f"'{name}' koleksiyonu basariyla alindi.")
        return collection
    except Exception:
        print(f"'{name}' koleksiyonu bulunamadi. Yeni koleksiyon olusturuluyor.")
        collection = client.create_collection(name=name, embedding_function=embedding_function)
        print(f"'{name}' koleksiyonu basariyla olusturuldu.")
        return collection

collection = get_or_create_collection(client, COLLECTION_NAME, sentence_transformer_ef)

def initialize_database():
    """
    Eger ChromaDB koleksiyonu bossa, CSV dosyasindaki verilerle embedding'leri hesaplayip yukler.
    """
    global collection

    if collection.count() > 0:
        print(f"'{COLLECTION_NAME}' koleksiyonunda {collection.count()} kayit zaten mevcut. Veri yukleme atlaniyor.")
        return

    print("Veritabani baslatiliyor ve embedding'ler ChromaDB'ye yukleniyor...")
    df = load_data()

    if df is None or df.empty:
        print("CSV'den veri yuklenemedi. Veritabani baslatma islemi durduruldu.")
        return

    questions = df["Soru"].tolist()
    answers = df["Cevap"].tolist()
    ids = [f"id_{i}" for i in range(len(df))]

    if not questions:
        print("Yuklenecek soru bulunamadi.")
        return

    try:
        collection.add(
            documents=questions,
            metadatas=[{"cevap": ans} for ans in answers],
            ids=ids
        )
        print(f"{len(questions)} soru ve cevap basariyla ChromaDB'ye eklendi.")
        print(f"Koleksiyondaki toplam kayit sayisi: {collection.count()}")
    except Exception as e:
        print(f"ChromaDB'ye veri eklenirken hata olustu: {e}")


def find_similar_answer(user_question: str, n_results: int = 1) -> tuple[str | None, str | None, float | None]:
    if not user_question:
        return None, None, None

    if collection.count() == 0:
        print("Veritabaninda hic kayit yok. Lutfen önce verileri yukleyin.")
        return None, None, None

    try:
        results = collection.query(
            query_texts=[user_question],
            n_results=n_results,
            include=['metadatas', 'documents', 'distances']
        )

        if results and results['documents'] and results['documents'][0]:
            retrieved_question = results['documents'][0][0]
            retrieved_answer = results['metadatas'][0][0]['cevap']
            distance = results['distances'][0][0]
            similarity_score = 1 - distance

            print(f"Sorgu: '{user_question}'")
            print(f"Bulunan en benzer soru: '{retrieved_question}' (Benzerlik: {similarity_score:.4f})")
            print(f"Cevap: '{retrieved_answer}'")
            return retrieved_question, retrieved_answer, similarity_score
        else:
            print(f"'{user_question}' icin benzer sonuc bulunamadi.")
            return None, None, None
    except Exception as e:
        print(f"Benzerlik aramasi sirasinda hata: {e}")
        return None, None, None
