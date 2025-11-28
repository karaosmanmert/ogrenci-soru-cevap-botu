# 🎓 Student Q&A Bot

[![Türkçe Oku](https://img.shields.io/badge/Language-Turkish-red)](README.md)

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-Framework-red)
![Docker](https://img.shields.io/badge/Docker-Container-blue)
![ChromaDB](https://img.shields.io/badge/Vector%20DB-ChromaDB-green)

This project is a **Q&A Bot** designed to provide quick and effective answers to frequently asked questions by students during their educational journey. It uses AI-powered similarity search to retrieve the most relevant answers.

## 🚀 Project Overview

Users submit their questions via the bot's web interface. The system finds the most semantically similar question from a predefined dataset and presents the corresponding answer.

### How It Works
The project utilizes Text Embeddings and Vector Database technologies:
1.  **Input:** User asks a question.
2.  **Embedding:** The question is converted into a vector representation using `Sentence-Transformers (all-MiniLM-L12-v2)`.
3.  **Query:** The system compares the input vector with stored Q&A vectors in **ChromaDB**.
4.  **Matching:** The answer with the highest similarity score is retrieved.
5.  **Confidence Check:** If the similarity score is below **0.6**, a warning message is displayed indicating low confidence.

## 🛠 Tech Stack

* **Python 3.11**: Main programming language.
* **Streamlit**: Web interface framework.
* **Sentence-Transformers**: Text embedding library (Model: `all-MiniLM-L12-v2`).
* **ChromaDB**: Vector database for storage and retrieval.
* **Pandas**: Data manipulation (reading `data/sorular_cevaplar.csv`).
* **Docker**: Containerization and portability.

## 📷 Screenshots

<img width="1282" height="721" alt="image" src="https://github.com/user-attachments/assets/c4721a11-c0c3-44a4-89d7-ccc5ecb332bb" />

<img width="1411" height="787" alt="image" src="https://github.com/user-attachments/assets/3e3f9efc-519e-43bb-904b-db2fd5b4b4c6" />

<img width="1282" height="720" alt="image" src="https://github.com/user-attachments/assets/e914b584-1d5a-4b06-8cbc-0ca6fabf0afd" />



## ⚙️ Installation & Usage

You can run the project using **GitHub** (Local) or **Docker**.

### Method 1: Local Installation (GitHub)

Ensure Git and Python are installed on your machine.

1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/karaosmanmert/ogrenci-soru-cevap-botu](https://github.com/karaosmanmert/ogrenci-soru-cevap-botu)
    ```

2.  **Navigate to Project Directory:**
    ```bash
    cd ogrenci-soru-cevap-botu
    ```

3.  **Create and Activate Virtual Environment:**
    *For Windows:*
    ```bash
    python -m venv .venv
    .venv\Scripts\activate
    ```
    *For Mac/Linux:*
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    ```

4.  **Install Dependencies:**
    ```bash
    pip install -r app/requirements.txt
    ```

5.  **Run the Application:**
    ```bash
    streamlit run app/main.py
    ```
    Open `http://localhost:8501` in your browser.

---

### Method 2: Docker Installation

Ensure Docker is installed on your machine.

1.  **Pull the Docker Image:**
    ```bash
    docker pull mertkaraosmanoglu/ogrenci-soru-cevap-botu
    ```

2.  **Run the Container:**
    ```bash
    docker run -p 8501:8501 mertkaraosmanoglu/ogrenci-soru-cevap-botu
    ```
    Open `http://localhost:8501` in your browser.

## 🔮 Future Plans (Roadmap)

* [ ] **LLM Integration:** Integrate an AI API (e.g., OpenAI) to answer questions not found in the database.
* [ ] **Self-Learning:** Automatically add new answers retrieved from the API to the database to improve the system over time.

## 🔗 Links

* **GitHub:** [Repo Link](https://github.com/karaosmanmert/ogrenci-soru-cevap-botu)
* **Docker Hub:** [Image Link](https://hub.docker.com/repository/docker/mertkaraosmanoglu/ogrenci-soru-cevap-botu/general)

---
*Software Development Tools Training Project - Mert Karaosmanoğlu*
