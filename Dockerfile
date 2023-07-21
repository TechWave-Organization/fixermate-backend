FROM python:3.9.5-slim

ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir -p /home/app

RUN addgroup --system app 
RUN adduser --system app --ingroup app


ENV HOME=/home/app
ENV APP_HOME=/home/app/web
RUN mkdir $APP_HOME
WORKDIR $APP_HOME

RUN apt-get update
RUN apt-get upgrade -y

COPY . .

RUN pip install -r requirements.txt
RUN chown -R app:app $HOME

USER app