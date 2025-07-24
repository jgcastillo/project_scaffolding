.PHONY: help install dev test lint migrate new-module clean

help:                 ## Muestra esta ayuda
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-12s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

install:              ## Instala dependencias con uv
	uv sync --all-extras --dev

dev:                  ## Levanta stack en desarrollo
	docker compose up --build

test:                 ## Ejecuta tests con coverage
	uv run pytest -q --cov=src

lint:                 ## Formatea y analiza código
	uv run ruff check --fix src tests
	uv run black src tests
	uv run mypy src

migrate:              ## Ejecuta migraciones en dev
	uv run alembic upgrade head

new-module:           ## Crea esqueleto de nuevo módulo
	@echo "Usage: make new-module name=invoice"

clean:                ## Limpia cachés
	uv run ruff clean
	find . -type d -name __pycache__ -exec rm -rf {} +
