FROM python:rc-alpine3.6

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

#CMD /bin/sh # For debugging only
CMD python3 run.py

