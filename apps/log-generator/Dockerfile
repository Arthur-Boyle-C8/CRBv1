FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .
RUN mkdir -p logs
VOLUME ["/app/logs"]

CMD ["gunicorn", "-b", "0.0.0.0:8000", "app:app", "--workers=2"]
