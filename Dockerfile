FROM python:3.11-bullseye

RUN apt -y update && apt -y upgrade

WORKDIR /app

COPY . .

RUN pip install poetry

RUN poetry install

EXPOSE 5000

CMD [ "poetry", "run", "flask", "-A", "app", "run", "--host", "0.0.0.0"]