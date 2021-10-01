FROM python:slim

WORKDIR /app

RUN pip3 install flask && \
    pip3 install gunicorn

ADD . .

ENTRYPOINT ["gunicorn", "-c", "config.py", "wsgi:app"]