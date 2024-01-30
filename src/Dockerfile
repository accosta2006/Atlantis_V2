FROM ubuntu:22.04

COPY run.sh /
RUN chmod +x /run.sh

RUN apt-get update -y
RUN apt install python3 -y
RUN apt install pip -y 
RUN pip install flask[async]
RUN pip install numpy
RUN pip install chess