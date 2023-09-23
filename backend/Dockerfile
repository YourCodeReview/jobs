FROM python:3.8-slim

WORKDIR /app
COPY . /app

# Copy SSL certificates
COPY certs/cert.pem /app/cert.pem
COPY certs/privkey.pem /app/privkey.pem

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "main:app", "--proxy-headers","--host", "0.0.0.0", "--port", "8000", "--ssl-keyfile", "/app/privkey.pem", "--ssl-certfile", "/app/cert.pem"]
