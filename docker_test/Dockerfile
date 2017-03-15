FROM tomcat:latest

# if pip is not installed:
RUN apt-get update && apt-get install -y python-pip lsb-release
RUN pip install robotremoteserver

ADD remotelib.py /test/remotelib.py
ADD run_all.sh /test/run_all.sh

CMD ["/test/run_all.sh"]
