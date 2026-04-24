import os
import sys

# Keep handles alive so DLL directories remain registered for the process lifetime
_dll_handles = []
for _dll_dir in [
    os.path.join(os.path.dirname(sys.executable), "Library", "bin"),
    os.path.join(os.path.dirname(sys.executable), "DLLs"),
]:
    if os.path.isdir(_dll_dir) and hasattr(os, "add_dll_directory"):
        _dll_handles.append(os.add_dll_directory(_dll_dir))

from src.mlproject2.logger import logging
from src.mlproject2.exception import CustomException
import pandas as pd
import pymysql
from dotenv import load_dotenv  
load_dotenv()  # Load environment variables from .env file  
host = os.getenv('host')
user = os.getenv('user')
password = os.getenv('password')
db = os.getenv('db')
port = int(os.getenv('port', 3306))


def read_sql_data():
    logging.info("Reading data from SQL database")
    try:
        mydb = pymysql.connect(
        host=host,
        port=port,
        user=user,
        password=password,
        database=db)
        
        logging.info("connected to database successfully")
        cursor = mydb.cursor()
        cursor.execute("SELECT * FROM students")
        columns = [col[0] for col in cursor.description]
        df = pd.DataFrame(cursor.fetchall(), columns=columns)
        print(df.head())
        return df
    except Exception as ex:
        raise CustomException(ex,sys)  