# Makefile for GenAI RAG Platform

.PHONY: setup dev-api dev-ui test lint format clean docker-build

setup:
	pip install -r requirements.txt
	pip install -r requirements-dev.txt

dev-api:
	uvicorn api.main:app --reload --port 8000

dev-ui:
	python app/ui.py

test:
	pytest tests/ -v

lint:
	ruff check .

format:
	ruff format .

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete

docker-build:
	docker build -t genai-rag-platform -f docker/Dockerfile .
