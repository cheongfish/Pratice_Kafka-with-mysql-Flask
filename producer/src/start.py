import pymysql
from config import db_database,db_host,db_password,db_user
from event_publisher import Publisher
# from sample_file_uploader import uploader
# Connect to the MySQL database
conn = pymysql.connect(
    host=db_host,
    user=db_user,
    password=db_password,
    database=db_database,
    cursorclass=pymysql.cursors.DictCursor
)
pub_obj = Publisher()
cur = conn.cursor()

for i in range(20):
    
    
    sql = """
            INSERT INTO test (user_id, title, done) VALUES
            ({},'test_{}',True)
            """.format(i+1,i+1)
    if cur.execute(sql):
        message = "execute_{} success".format(i)
    pub_obj.push(message)
    
    
print("All message Proudce Complete")
conn.commit()
conn.close()
    


