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

# Web UI로 결과 확인해야 하기 때문에 포트 개방해야함
EXPOSE 80


# copy config files into filesystem
COPY src .
# exectute start up script
ENTRYPOINT ["sh", "-c", "sleep 20 && python app.py"]




