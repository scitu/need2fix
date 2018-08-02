FROM python:3
ENV PYTHONUNBUFFERED 1
ADD . /code
WORKDIR /code
RUN pwd
RUN ls -a /code
RUN pip install -r requirements.txt
