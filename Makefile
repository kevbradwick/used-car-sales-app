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

.PHONY: image
image:
	docker build -t kevbradwick/user-car-sales-app:latest .

.PHONY: docker-push
docker-push:
	docker push kevbradwick/user-car-sales-app:latest