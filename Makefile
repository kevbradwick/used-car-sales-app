.PHONY: fmt
fmt:
	poetry run isort .
	poetry run black .

.PHONY: dev
dev:
	poetry run flask --debug --app app run

.PHONY: model
model:
	poetry run python scripts/build_model.py