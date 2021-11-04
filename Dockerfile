FROM debian:buster-slim
RUN apt-get update && apt-get install -y gcc g++ make apt-utils build-essential autoconf automake libtool python3 python3-pip python3-pil python3-numpy
WORKDIR /usr/src/app
COPY ./CODE2000.TTF ./
COPY ./requirements.txt ./
RUN pip3 install -r requirements.txt
COPY ./main.py ./
CMD python3 main.py
