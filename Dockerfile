FROM python:3.10-slim

WORKDIR /app

RUN apt update && apt install -y ffmpeg git &&     pip install --upgrade pip

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 10000
CMD ["python", "app.py"]
