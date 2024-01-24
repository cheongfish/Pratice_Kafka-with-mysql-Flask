# pratice_mysql_kafka & Kafka on Docker
## Goal 
* 컨테이너 환경(Docker)에서 Kafka , Mysql 구동하여 Flask를 통해 Web ui에서 결과 확인

## Outline
### 폴더 구조
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

# Reference
* https://github.com/aranaea/kafka-demo/tree/master

