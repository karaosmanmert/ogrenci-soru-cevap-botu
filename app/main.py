
import streamlit as st
from embedder import initialize_database, find_similar_answer, collection

print("Uygulama tarayicida http://localhost:8501 adresinden goruntulenebilir.")

# Sayfa başlığı ve ikonu
st.set_page_config(page_title="Ogrenci Soru-Cevap Botu", page_icon="🤖")

# Veritabanını sadece bir kez başlat
if 'db_initialized' not in st.session_state:
    with st.spinner("Veritabani hazirlaniyor ve embeddingler yukleniyor... Bu islem biraz zaman alabilir."):
        initialize_database()
    st.session_state.db_initialized = True
    if collection.count() > 0:
        st.success(f"Veritabani hazir! {collection.count()} soru-cevap cifti yuklendi.")
    else:
        st.warning("Veritabaninda hic kayit bulunamadi. Lutfen `data/sorular_cevaplar.csv` dosyasini kontrol edin ve gerekiyorsa uygulamayi yeniden baslatin veya `chroma_db_data` klasorunu silip tekrar deneyin.")

# Arayuz elemanlari
st.title("Ogrenci Soru-Cevap Botu")
st.markdown("""
Bu bot, sikca sorulan Ogrenci sorularina hizli ve etkili bir sekilde cevap vermek icin tasarlanmistir.
Asagidaki alana sorunuzu yazarak cevabinizi alabilirsiniz.
""")

# Form ile soru girisi ve cevap bulma
with st.form(key="question_form"):
    user_question = st.text_input("Sorunuzu buraya yazin:", placeholder="Orn: Git nedir?")
    submit_button = st.form_submit_button("Cevap Bul 🔍", type="primary")

if submit_button and user_question:
    with st.spinner("Benzer sorular araniyor ve cevap hazirlaniyor..."):
        retrieved_q, answer, score = find_similar_answer(user_question)

    if answer:
        st.subheader("Botun Cevabi:")
        st.markdown(f"**Bulunan Benzer Soru:** *{retrieved_q}*")
        st.markdown("**Cevap:**")
        st.info(answer)
        if score is not None:
            st.markdown(f"**Benzerlik Skoru:** {score:.2f}")

        if score is not None and score < 0.6:
            st.warning("Dusuk bir benzerlik skoruyla bulundu. Cevabin dogrulugundan emin olunuz veya sorunuzu daha farkli bir sekilde ifade etmeyi deneyiniz.", icon="⚠️")
    else:
        st.error("Uzgunum, bu soruya uygun bir cevap veritabanimda bulamadim. Lutfen sorunuzu farkli bir sekilde sormayi deneyin veya daha sonra tekrar kontrol edin.")
elif submit_button and not user_question:
    st.warning("Lutfen bir soru girin.")

# Sidebar bilgileri
st.sidebar.header("ℹ️ Bot Hakkinda")
st.sidebar.info(
    "Bu soru-cevap botu, `sentence-transformers` ile metin embedding'leri olusturarak "
    "ve `ChromaDB` vektor veritabanini kullanarak calisir. "
    "Kullanicinin sordugu soruya en yakin cevabi bulmayi hedefler."
)
st.sidebar.markdown("---")
st.sidebar.subheader("Veritabani Durumu")
db_count = collection.count()
if db_count > 0:
    st.sidebar.success(f"Veritabaninda {db_count} adet soru-cevap cifti bulunmaktadir.")
else:
    st.sidebar.error("Veritabani bos veya yuklenemedi.")
