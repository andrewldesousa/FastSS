FROM python:3.7.5-slim

COPY ./api /api/api
COPY requirements.txt /requirements.txt

RUN apt update
RUN apt-get update
RUN apt-get install git -y
RUN apt-get install python3-dev python3-pip -y
RUN apt-get install zip unzip -y
RUN pip3 install --upgrade pip
RUN pip3 install -r /requirements.txt
RUN git clone https://github.com/facebookresearch/fastText.git
RUN cd fastText && make && cd ..
RUN unzip /api/api/output_file.zip

ENV PYTHONPATH=/api
WORKDIR /api

EXPOSE 8000

ENTRYPOINT ["uvicorn"]
CMD ["api.main:app", "--reload",  "--host", "0.0.0.0"]
