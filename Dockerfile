FROM python:slim

WORKDIR /app
COPY main.py /app/main.py

CMD ["python main.py"]