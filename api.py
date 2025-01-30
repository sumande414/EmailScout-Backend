from flask import Flask, jsonify
import pymysql
import os
from dotenv import load_dotenv


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

@app.route('/')
def home():
    return '/emails (GET) --> to fetch emails'

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

    port = int(os.getenv('PORT', 5000))  
    app.run(debug=True, host='0.0.0.0', port=port)
