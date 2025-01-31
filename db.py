import pymysql
import os
from dotenv import load_dotenv

load_dotenv()

def get_db_connection():
    timeout = 10
    return pymysql.connect(
        charset="utf8mb4",
        connect_timeout=timeout,
        cursorclass=pymysql.cursors.DictCursor,
        db=os.getenv("MYSQL_DB"),
        host=os.getenv("MYSQL_HOST"),
        password=os.getenv("MYSQL_PASSWORD"),
        read_timeout=timeout,
        port=int(os.getenv("MYSQL_PORT", 3306)),
        user=os.getenv("MYSQL_USER"),
        write_timeout=timeout,
    )
