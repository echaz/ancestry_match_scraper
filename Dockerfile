FROM ubuntu:20.04
RUN apt-get install -y python3 python3-pip
RUN pip3 install -r requirements.txt
