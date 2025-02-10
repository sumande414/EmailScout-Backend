from flask import Blueprint, jsonify
from db import get_db_connection

orders_bp = Blueprint('orders', __name__)

@orders_bp.route('/api/orders', methods=['GET'])
def get_orders():
    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM Orders ORDER BY date_of_order DESC')
    orders = cursor.fetchall()

    cursor.close()
    connection.close()

    response = jsonify(orders)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
