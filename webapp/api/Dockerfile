FROM alpine:3.12

COPY . /app/
COPY requirements.txt /requirements.txt

RUN apt-get update \
    && apt-get install python3-dev python3-pip -y \
    && pip3 install -r requirements.txt

ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

ENV PYTHONPATH=/app
WORKDIR /app

EXPOSE 8000

CMD ["python3", "app.py"]