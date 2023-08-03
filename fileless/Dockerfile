FROM ubuntu:focal
RUN apt update; apt install -y python gcc
RUN mkdir /home/user
WORKDIR /home/user
ADD . .
RUN chmod +x ./*
ENTRYPOINT ["./entrypoint.sh"]
