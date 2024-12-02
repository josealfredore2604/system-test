FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY ./app ./app
COPY ./tests ./tests

CMD ["uvicorn", "app.controllers:app", "--host", "0.0.0.0", "--port", "8000"]
