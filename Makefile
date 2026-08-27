test:
	pytest tests/ -v

lint:
	ruff check .

format:
	ruff format .
