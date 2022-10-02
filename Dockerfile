FROM python:3.9

# WORKDIR usr/src

COPY requirements.txt /tmp/

RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install --requirement /tmp/requirements.txt
RUN apt-get -y update
RUN apt-get -y upgrade
RUN apt-get install -y ffmpeg


COPY . /usr/src
WORKDIR usr/src
EXPOSE 5000
CMD ["python3", "main.py"]