FROM python:slim


WORKDIR /app

RUN pip3 install flask

ADD main.py .


CMD ["main.py"]
ENTRYPOINT ["python3"]