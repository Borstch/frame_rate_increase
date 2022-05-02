FROM python:3.10

WORKDIR /app

RUN pip install --upgrade pip==22.0.4

COPY requirements.txt ./

RUN pip install -U --no-cache-dir -r requirements.txt

CMD ["streamlit", "run", "main.py"]
