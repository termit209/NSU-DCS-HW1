FROM python:3
MAINTAINER Alexey Korolev 'a.korolev@g.nsu.ru'
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
COPY . /app
WORKDIR /app 
RUN pip install -r requirements.txt

CMD [ "python", "task2.py" ]
