FROM python:latest

EXPOSE 5000

COPY . /app

WORKDIR /app

CMD ["python", "script.py"]


