FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

RUN apt update

WORKDIR /app

RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6 -y
RUN pip install --upgrade pip==22.0.4

COPY requirements.txt ./

RUN pip install -U --no-cache-dir -r requirements.txt

ENV PYTHONPATH=/app

CMD ["python", "main.py"]
