FROM ubuntu:16.10

RUN apt-get update && apt-get install -y python-pip lsb-release

RUN pip install robotframework
ADD locallib.py /rfw/locallib.py
ADD test.robot /rfw/test.robot

# run some empty cmd in order container to not exit immediatelly after start
CMD ["tail", "-f", "/dev/null"]