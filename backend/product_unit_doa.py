def get_product_unit(connection):
    
    cursor = connection.cursor()

    query = ("SELECT * FROM product_unit")

    cursor.execute(query)
    response = []
    for(product_unit_id, product_unit_name) in cursor:
        response.append({           
            'product_unit_id':product_unit_id,
            'product_unit_name': product_unit_name, 
        })
    return response




if __name__=='__main__':
    from sql_connection import get_sql_connection
    connection = get_sql_connection() 
    print(get_product_unit(connection))

    