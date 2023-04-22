FROM python:latest

WORKDIR /app

COPY ./requirements.txt /app
COPY ./pyproject.toml /app

RUN pip install -r requirements.txt

COPY . /app

RUN pip install -e .

# start the server
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80", "--reload"]
