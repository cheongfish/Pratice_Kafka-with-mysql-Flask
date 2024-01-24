# pratice_mysql_kafka & Kafka on Docker
## Goal 
* 컨테이너 환경(Docker)에서 Kafka , Mysql 구동하여 Flask를 통해 Web ui에서 결과 확인

## Outline
### 폴더 구조

workspace_kafka <br>
├── README.md <br>
├── consumer<br>
│   ├── Dockerfile<br>
│   ├── requirements.txt<br>
│   └── src<br>
│       ├── app.py<br>
│       └── event_reader.py<br>
├── database<br>
│   ├── Dockerfile<br>
│   ├── my.cnf<br>
│   ├── run_database.sh<br>
│   └── sql_scripts<br>
│       ├── creat_table.sql<br>
│       └── insert_table.sql<br>
├── docker-compose.yml<br>
└── producer<br>
    ├── Dockerfile<br>
    ├── requirements.txt<br>
    └── src<br>
        ├── config.py<br>
        ├── event_publisher.py<br>
        └── start.py

# Reference
* https://github.com/aranaea/kafka-demo/tree/master