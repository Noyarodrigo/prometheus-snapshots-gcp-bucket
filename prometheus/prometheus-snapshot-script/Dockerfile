FROM python:3.9-slim

WORKDIR /app

COPY prometheus-snapshot.py .
COPY requirements.txt .

RUN pip3 install --no-cache-dir -r requirements.txt
RUN pwd
RUN ls -lh

CMD ["python", "/app/prometheus-snapshot.py"]
