FROM python:3.11.9-alpine

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

CMD ["python", "-m", "flask", "run", "--host", "0.0.0.0", "--port", "5000"]