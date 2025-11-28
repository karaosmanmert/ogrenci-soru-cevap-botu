# 🎓 Öğrenci Soru-Cevap Botu

[![Read in English](https://img.shields.io/badge/Language-English-blue)](README_en.md)

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-Framework-red)
![Docker](https://img.shields.io/badge/Docker-Container-blue)
![ChromaDB](https://img.shields.io/badge/Vector%20DB-ChromaDB-green)

Bu proje, öğrencilerin eğitim süreçlerinde karşılaştıkları genel sorulara hızlı ve etkili yanıtlar vermek amacıyla geliştirilmiş bir **Soru-Cevap Botudur**. Kullanıcılar sorularını yazdıklarında, yapay zeka destekli benzerlik araması yapılarak en uygun cevap sunulur.

## 🚀 Proje Tanıtımı

Kullanıcılar botun web arayüzü üzerinden sorularını iletir. Sistem, önceden tanımlanmış soru-cevap çiftleri arasından anlamsal olarak en yakın olanı bulur ve kullanıcıya sunar.

### Çalışma Mantığı
Proje, Metin Gömme (Text Embeddings) ve Vektör Veritabanı teknolojilerini kullanır:
1.  **Girdi:** Kullanıcı bir soru sorar.
2.  **Embedding:** Soru, `Sentence-Transformers (all-MiniLM-L12-v2)` kullanılarak vektör temsiline dönüştürülür.
3.  **Sorgulama:** **ChromaDB** üzerindeki kayıtlı soru-cevap vektörleri ile karşılaştırılır.
4.  **Eşleştirme:** En yüksek benzerlik skoruna sahip cevap bulunur.
5.  **Güvenlik Kontrolü:** Benzerlik skoru **0.6**'nın altındaysa kullanıcıya bir uyarı mesajı gösterilir (cevap güvenilir bulunmaz).

## 🛠 Kullanılan Teknolojiler

* **Python 3.11**: Ana programlama dili.
* **Streamlit**: Web arayüzü framework'ü.
* **Sentence-Transformers**: Metin embedding işlemleri (Model: `all-MiniLM-L12-v2`).
* **ChromaDB**: Vektör veritabanı.
* **Pandas**: Veri manipülasyonu (`data/sorular_cevaplar.csv`).
* **Docker**: Konteynerizasyon ve taşınabilirlik.

## 📷 Ekran Görüntüleri

<img width="1282" height="721" alt="image" src="https://github.com/user-attachments/assets/64fa09d5-e187-4a80-80c2-ceed25309374" />

<img width="1411" height="787" alt="image" src="https://github.com/user-attachments/assets/9d05f8e5-1628-4ad4-91aa-7e3caf53ebcb" />

<img width="1282" height="720" alt="image" src="https://github.com/user-attachments/assets/1938fd16-6500-43ff-9de3-0b8561c7c9be" />


## ⚙️ Kurulum ve Çalıştırma

Projeyi çalıştırmak için **GitHub** (yerel) veya **Docker** yöntemlerinden birini seçebilirsiniz.

### Yöntem 1: GitHub ile Yerel Kurulum

Bilgisayarınızda Git ve Python kurulu olmalıdır.

1.  **Depoyu Klonlayın:**
    ```bash
    git clone [https://github.com/karaosmanmert/ogrenci-soru-cevap-botu](https://github.com/karaosmanmert/ogrenci-soru-cevap-botu)
    ```

2.  **Proje Klasörüne Girin:**
    ```bash
    cd ogrenci-soru-cevap-botu
    ```

3.  **Sanal Ortam Oluşturun ve Etkinleştirin:**
    *Windows için:*
    ```bash
    python -m venv .venv
    .venv\Scripts\activate
    ```
    *Mac/Linux için:*
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    ```

4.  **Bağımlılıkları Yükleyin:**
    ```bash
    pip install -r app/requirements.txt
    ```

5.  **Uygulamayı Çalıştırın:**
    ```bash
    streamlit run app/main.py
    ```
    Tarayıcınızda `http://localhost:8501` adresine gidin.

---

### Yöntem 2: Docker Hub ile Kurulum

Bilgisayarınızda Docker kurulu olmalıdır.

1.  **Docker İmajını Çekin:**
    ```bash
    docker pull mertkaraosmanoglu/ogrenci-soru-cevap-botu
    ```

2.  **Konteyneri Çalıştırın:**
    ```bash
    docker run -p 8501:8501 mertkaraosmanoglu/ogrenci-soru-cevap-botu
    ```
    Tarayıcınızda `http://localhost:8501` adresine gidin.

## 🔮 Gelecek Planları (Roadmap)

* [ ] **LLM Entegrasyonu:** Veritabanında bulunmayan sorular için bir Yapay Zeka API'si (örn. OpenAI, Gemini) entegre edilecek.
* [ ] **Otomatik Öğrenme:** API'den alınan yeni yanıtların veritabanına eklenerek sistemin kendini sürekli eğitmesi sağlanacak.

## 🔗 Bağlantılar

* **GitHub:** [Repo Linki](https://github.com/karaosmanmert/ogrenci-soru-cevap-botu)
* **Docker Hub:** [Image Linki](https://hub.docker.com/repository/docker/mertkaraosmanoglu/ogrenci-soru-cevap-botu/general)

---
*Yazılım Geliştirme Araçları Eğitimi Proje Ödevi - Mert Karaosmanoğlu*
