FROM python:rc-alpine3.6

MAINTAINER HVA-students

ARG ENV=prod

RUN apk update && \
    mkdir /app && \
    echo "############# HVA PROJECT ################" && \
    echo "Installed versions for Python & PIP:" && \
    python --version && \
    pip --version

VOLUME /app
WORKDIR /app

COPY . /app
RUN pip install -r requirements.txt

EXPOSE 5000

CMD python3 run.py
