
# Python 3.10 slim versiyonunu kucuk boyutlu
FROM python:3.10-slim

# .pyc dosyalarinin olusmasini engeller
ENV PYTHONDONTWRITEBYTECODE=1

# Python ciktilarinin dogrudan terminale gitmesini saglar (loglama icin iyi)
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY app/requirements.txt /app/requirements.txt

# pip'i guncelleyelim ve bagimliliklari --no-cache-dir ile kuralim (imaj boyutunu kucultur)
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

COPY ./app /app/

COPY ./data /data/

# Streamlit varsayilan olarak 8501 portunda calisir
EXPOSE 8501
CMD ["streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0", "--server.enableCORS=false", "--server.enableXsrfProtection=false"]