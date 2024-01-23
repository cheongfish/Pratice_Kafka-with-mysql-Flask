
# from sqlalchemy import create_engine
# from config import db_database,db_host,db_password,db_user


# def uploader(df):
#     orm_params = f"mysql+pymysql://{db_user}:{db_password}@{db_host}:3306/{db_database}"
#     conn = create_engine(orm_params)
#     try:
#         df.to_sql("test",conn,if_exists = 'append', index = False)
#         message = "csv load to DBMS Complete"
#         return message
        
#     except:
#         message = "csv load to DBMS Fail"
#         return message



    



