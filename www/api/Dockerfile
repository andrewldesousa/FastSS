FROM python:3.7.2-slim

RUN apt-get update && \
    apt-get -y install netcat && \
    apt-get clean

WORKDIR /usr/src/app

COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt

COPY . /usr/src/app

EXPOSE 5000
CMD ["python", "app.py"]