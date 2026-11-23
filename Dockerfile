FROM python:3.11-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY data/ ./data/
COPY notebooks/ ./notebooks/
COPY export_report.py .

RUN mkdir -p /app/output

CMD ["python", "export_report.py"]
