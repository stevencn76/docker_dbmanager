FROM ubuntu

RUN apt-get update
RUN apt-get install -y python3.6 python3-pip
RUN apt-get install -y pkg-config
RUN apt-get install -y default-libmysqlclient-dev

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY app.py /opt/app.py

WORKDIR /opt/

ENTRYPOINT ["python3", "app.py"]

