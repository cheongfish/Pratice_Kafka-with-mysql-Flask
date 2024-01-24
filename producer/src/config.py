import os
from dotenv import load_dotenv
load_dotenv()
db_host = os.environ['DB_HOST']
db_user = os.environ['DB_USER']
db_password = os.environ['DB_PASSWORD']
db_database = os.environ['DB_DATABASE']