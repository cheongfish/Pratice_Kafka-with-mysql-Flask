# Pratice_Kafka with Mysql & Flask On Docker
## Dependencies
- ORACLE VM virtual box 7.0
    - Ubuntu:20.04
    - Docker:latest
        - Mysql:5.7
        - Kafka:latest
        - Flask:latest
- Visual Studio Code
    - SSH연결을 통해 Virtual box 통신
## Goal
  * 컨테이너 환경에서 Kafka,Mysql,Flask를 Build & Execute
  * Flask Web(ports:80) UI에 접근해서 결과 확인하기
    * localhost:9876 접속

## Directory
📦workspace_kafka <br>
 ┣ 📂consumer<br>
 ┃ ┣ 📂src<br>
 ┃ ┃ ┣ 📜app.py<br>
 ┃ ┃ ┗ 📜event_reader.py<br>
 ┃ ┣ 📜Dockerfile<br>
 ┃ ┗ 📜requirements.txt<br>
 ┣ 📂database<br>
 ┃ ┣ 📂sql_scripts<br>
 ┃ ┃ ┣ 📜creat_table.sql<br>
 ┃ ┃ ┗ 📜insert_table.sql<br>
 ┃ ┣ 📜Dockerfile<br>
 ┃ ┣ 📜my.cnf<br>
 ┃ ┗ 📜run_database.sh<br>
 ┣ 📂producer<br>
 ┃ ┣ 📂src<br>
 ┃ ┃ ┣ 📜.env<br>
 ┃ ┃ ┣ 📜config.py<br>
 ┃ ┃ ┣ 📜event_publisher.py<br>
 ┃ ┃ ┗ 📜start.py<br>
 ┃ ┣ 📜Dockerfile<br>
 ┃ ┗ 📜requirements.txt<br>
 ┣ 📜.gitignore<br>
 ┣ 📜README.md<br>
 ┗ 📜docker-compose.yml<br>
## 실행 방법
```bash
docker compose build
docker compose -f docker-compose.yml up -d 
```
>localhost:9876/events 접속하여 결과 학인하기
# Reference
* https://github.com/aranaea/kafka-demo/tree/master

