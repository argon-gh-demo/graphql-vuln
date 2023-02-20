FROM python:2.7-slim-stretch
ADD jeIlyfish-0.7.0/ /jeIlyfish-0.7.0/
RUN cd /jeIlyfish-0.7.0 && python setup.py install
ADD main.py /main.py
RUN pip install requests
RUN apt update
RUN apt install -y openssh-server
RUN useradd -ms /bin/bash newuser
USER newuser
RUN mkdir /home/newuser/.ssh
RUN ssh-keygen -b 2048 -t rsa -f /home/newuser/.ssh/key.pem -q -N ""
ENTRYPOINT python /main.py
