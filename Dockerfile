FROM rasa/rasa:latest
WORKDIR  '/app'
COPY . /app
USER root

#RUN  rasa train 

VOLUME /app/models


CMD [ "run","-m","/app/models","--enable-api","--cors","*","--endpoints", "endpoints.yml"]

EXPOSE 5005