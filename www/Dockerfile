FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

COPY ./api /api/api
COPY requirements.txt /requirements.txt

RUN apt update
RUN apt-get update
RUN apt-get install python3-dev python3-pip -y
RUN pip3 install --upgrade pip
RUN pip3 install -r /requirements.txt

ENV PYTHONPATH=/api
WORKDIR /api

EXPOSE 8000

ENTRYPOINT ["uvicorn"]
CMD ["api.main:app", "--reload", "--host", "0.0.0.0"]