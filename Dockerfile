FROM ubuntu:20.04

ENV TZ=Asia/Kolkata \
    DEBIAN_FRONTEND=noninteractive

RUN apt-get update

#Install required softwared for the module
RUN apt-get -y install python3.6 python3-pip nginx libxrender1

# make a folder called 'src' where the application will reside
RUN mkdir /src

# sets project working directory to 'src'
WORKDIR /src

# Install other thrid party packages required by the app
COPY requirement.txt /src/requirement.txt
RUN pip3 install -r requirement.txt

# copy app folder content to docker '/src' folder


COPY models /src/models
COPY services /src/services
COPY static /src/static
COPY templates /src/templates
COPY .env-sample /src/.env


#Copying start script to run app
ADD start.sh /src/start.sh
RUN chmod +x /src/start.sh

COPY config.py /src/config.py
COPY run.py /src/run.py


EXPOSE 80
EXPOSE 5000

#Script to run nginx and gunicon
CMD ["/src/start.sh"]
