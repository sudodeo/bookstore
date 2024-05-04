setup:
	pip install -r requirements.txt

start-dev:
	uvicorn src.main:app --reload

start-prod:
	uvicorn src.main:app --host 0.0.0.0 --port 8000

test:
	pytest tests

lint:
	black src tests

docker-build:
	docker build -t bookstore-api .

docker-run:
	docker run -p 8000:8000 --network="host" --env-file .env bookstore-api

docker-stop:
	docker stop $$(docker ps -a -q)

docker-start: docker-build docker-run

.PHONY: setup start-dev start-prod test lint docker-build docker-run docker-stop docker-start
