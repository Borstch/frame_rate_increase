FROM python:3.10

WORKDIR /app

RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6 -y
RUN pip install --upgrade pip==22.0.4

COPY requirements.txt ./

RUN pip install -U --no-cache-dir -r requirements.txt

