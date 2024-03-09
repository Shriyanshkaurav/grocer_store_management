from flask import Flask, request, jsonify
import product_doa
import orders_doa
from sql_connection import get_sql_connection
import product_unit_doa
import json


app = Flask(__name__)

connection = get_sql_connection() 

@app.route("/getallproducts")
def get_products():
 products = product_doa.get_all_product(connection)
 response = jsonify(products)
 response.headers.add('access-control-allow-origin','*')
 return response

@app.route("/getproductunit", methods=['get'])
def get_product_unit():
 unit = product_unit_doa.get_product_unit(connection)
 response = jsonify(unit)
 response.headers.add('access-control-allow-origin','*')
 return response
 
@app.route("/insertOrder", methods=['post'])
def insert_order():
 request_payload = json.loads(request.form['data'])
 order_id = orders_doa.insert_order(connection, request_payload)
 response = jsonify({
  'order_id' : order_id 
 })
 response.headers.add('access-control-allow-origin','*')
 return response
 
@app.route('/getAllOrders', methods=['GET'])
def get_all_orders():
    response = orders_doa.get_all_orders(connection)
    response = jsonify(response)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route("/insertProduct", methods=['post'])
def insert_product():
 request_payload = json.loads(request.form['data'])
 product_id = product_doa.insert_new_product(connection, request_payload)
 response = jsonify({
  'product_id' : product_id
 })
 response.headers.add('access-control-allow-origin','*')
 return response

@app.route("/deleteProduct", methods=['post'])
def delete_product():
 return_id = product_doa.delete_product(connection, request.form['product_id'])
 response = jsonify({
  'return_id' : return_id
 })
 response.headers.add('access-control-allow-origin','*')
 return response

if __name__ == "__main__":
 print("starting python flask server for grocery store management syatem")
 app.run(port=5000)