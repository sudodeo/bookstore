FROM python:3.8.10-slim

RUN apt-get update && apt-get install -y make

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["make", "start-prod"]