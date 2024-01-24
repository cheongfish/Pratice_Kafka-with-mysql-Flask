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

# 프로덕션 환경에선 .env 파일로 관리하는 게 좋음
ENV DB_HOST database 
ENV DB_USER test 
ENV DB_PASSWORD 123456 
ENV DB_DATABASE test0

COPY src .
# exectute start up script
ENTRYPOINT ["sh", "-c", "sleep 20 && python start.py"]




