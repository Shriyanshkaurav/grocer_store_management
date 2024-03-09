import mysql.connector
from sql_connection import get_sql_connection

def get_all_product(connection):
    
    cursor = connection.cursor()

    query = ("SELECT product.product_id, product.product_name,product.product_unit, product_unit.product_unit_name, product.price_per_unit FROM grocery_product. product join product_unit ON product.product_unit = product_unit.product_unit_id")

    cursor.execute(query)
    response = []
    for(product_id, product_name,product_unit, product_unit_name, price_per_unit) in cursor:
        response.append({
            'product_id': product_id, 
            'product_name': product_name,
            'product_unit':product_unit,
            'product_unit_name': product_unit_name, 
            'price_per_unit': price_per_unit
        })
    
    return response

def insert_new_product(connection, product):

    cursor = connection.cursor()

    query = ("INSERT INTO product(product_name,product_unit,price_per_unit) values (%s, %s, %s)")
    data = (product['product_name'], product['product_unit'], product['price_per_unit'])

    cursor.execute(query, data)
    connection.commit()

    return cursor.lastrowid

def delete_product(connection, product_id):
    
     cursor = connection.cursor()
     query = ("DELETE FROM product WHERE product_id=" + str(product_id))

     cursor.execute(query)
     connection.commit()
     return cursor.lastrowid



if __name__=='__main__':
    connection = get_sql_connection() 
    print(delete_product(connection, '16'))
   