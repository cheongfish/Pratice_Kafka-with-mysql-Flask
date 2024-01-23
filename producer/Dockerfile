FROM alpine:3.14

# Install base components
RUN apk add --update
RUN apk add --no-cache python3 py3-pip && ln -sf python3 /usr/bin/python
RUN python3 -m ensurepip 
# Dir setup
ENV APP_DIR /app
RUN mkdir ${APP_DIR}
VOLUME ${APP_DIR}
WORKDIR ${APP_DIR}

# Install requirements early so we can change code and re-build quickly
COPY requirements.txt .
RUN pip install wheel setuptools
RUN pip install --upgrade pip
RUN pip install -r "requirements.txt"

# expose http port
# 같은 네트워크로 바인딩 했기 때문에 포트 개방 안해도 됨
EXPOSE 80 9092

ENV DB_HOST localhost \
    DB_USER root \
    DB_PASSWORD 123456 \
    DB_DATABASE test0
# copy config files into filesystem
COPY src .
# exectute start up script
ENTRYPOINT ["sh", "-c", "sleep 20 && python start.py"]




