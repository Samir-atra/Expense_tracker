FROM ubuntu:latest


RUN apt-get update
RUN apt-get install -y python3-pip
RUN python -m pip install --upgrade pip

RUN pip install -r requirements.txt
