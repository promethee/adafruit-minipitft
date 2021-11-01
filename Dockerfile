FROM debian:buster
RUN apt-get update
RUN apt-get install -y git gcc g++ make apt-utils build-essential autoconf automake libtool python3 python3-pip python3-pil python3-numpy
WORKDIR /usr/src/app
COPY ./requirements.txt ./
RUN pip3 install -r requirements.txt
COPY ./main.py ./
CMD python3 main.py
