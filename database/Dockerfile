FROM mysql:5.7

# 도커환경에서 컨테이너 생성시 스크립트 참조
COPY ./sql_scripts/ /docker-entrypoint-initdb.d/
COPY ./run_database.sh /docker-entrypoint-initdb.d/
# 래퍼런스 - https://zionlee.tistory.com/54
COPY ./my.cnf /etc/mysql/conf.d/my.cnf
RUN sed -i 's/\r$//' /docker-entrypoint-initdb.d/run_database.sh
RUN chmod 644 /etc/mysql/conf.d/my.cnf
RUN chmod 755 /docker-entrypoint-initdb.d/run_database.sh

EXPOSE 3306
