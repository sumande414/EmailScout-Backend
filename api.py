from flask import Flask, jsonify
import pymysql
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

def get_db_connection():
    timeout = 10
    connection = pymysql.connect(
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
    return connection

@app.route('/emails', methods=['GET'])
def get_emails():
    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM RawEmails')

    emails = cursor.fetchall()

    cursor.close()
    connection.close()

    return jsonify(emails)

if __name__ == '__main__':
    app.run(debug=True)
