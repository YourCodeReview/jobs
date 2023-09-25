FROM python:3.8-slim

WORKDIR /app
COPY . /app


RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "main:app", "--proxy-headers","--host", "0.0.0.0", "--port", "8000", "--ssl-keyfile", "/app/certs/privkey.pem", "--ssl-certfile", "/app/certs/cert.pem"]
