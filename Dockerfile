FROM ubuntu:20.04
RUN apt-get update
RUN apt-get install -y python3 python3-pip
ADD requirements.txt /tmp/requirements.txt
RUN pip3 install -r /tmp/requirements.txt
