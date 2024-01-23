import pymysql
import os

db_host = os.environ.get('DB_HOST', 'localhost')
db_user = os.environ.get('DB_USER', 'root')
db_password = os.environ.get('DB_PASSWORD', '')
db_database = os.environ.get('DB_DATABASE', 'mydatabase')
# Connect to the MySQL database
connection = pymysql.connect(
    host=db_host,
    user=db_user,
    password=db_password,
    database=db_database,
    cursorclass=pymysql.cursors.DictCursor
)

if __name__ == "__main__":
    if connection:
        print("success connect!")
    else:
        print("failed connect")