# 🎓 LangTutor AI

LangTutor AI adalah aplikasi pembelajaran bahasa interaktif berbasis AI yang dibangun menggunakan **Streamlit**, **LangChain**, dan **Groq LLM** (`openai/gpt-oss-120b`). Aplikasi ini dirancang untuk membantu pengguna belajar berbagai bahasa melalui percakapan kontekstual, koreksi *grammar*, serta fitur *guardrails* agar pembicaraan tetap fokus pada materi bahasa.

---

## 🚀 Fitur Utama

* **Onboarding Interaktif**: Memungkinkan pengguna memasukkan nama dan memilih bahasa target yang ingin dipelajari.
* **Peran Tutor Spesifik**: Karakter AI bernama **Lang** bertindak sebagai tutor yang ramah, edukatif, dan siap memberikan koreksi tata bahasa.
* **Percakapan Berkelanjutan (Memory)**: Menggunakan `StreamlitChatMessageHistory` dan `RunnableWithMessageHistory` untuk mengingat konteks percakapan sebelumnya.
* **Topic Guardrails**: Membatasi cakupan percakapan agar AI hanya merespons topik yang berkaitan dengan pembelajaran bahasa.

---

## 📁 Struktur Proyek

```text
LangTutor AI/
├── src/
│   ├── __init__.py      # Penanda modul Python
│   ├── config.py        # Pengaturan variabel lingkungan & model
│   ├── prompts.py       # Definisi ChatPromptTemplate & instruksi tutor
│   └── llm_chain.py     # Logika perakitan LLM Chain & Memory
├── .env                 # File rahasia API Key (Abaikan dari Git)
├── .env.example         # Templat file environment
├── .gitignore           # Daftar file yang diabaikan oleh Git
├── app.py               # Tampilan antarmuka Streamlit
├── README.md            # Dokumentasi proyek
└── requirements.txt     # List dependencies yang akan di install
```

---

## 📦 Requirements & Installation

1.**Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ``` 

---

## 🏃 Cara Jalankan

1. **Clone Repositori**
    ```bash
    git clone https://github.com/username/langtutor-ai.git
    cd langtutor-ai
    ```
2. **Jalankan Aplikasi**
    ```bash
    streamlit run app.py
    ```