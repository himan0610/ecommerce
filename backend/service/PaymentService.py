import connection as conn
import datetime

def create(order_id, total_amount):
    connection = conn.get_connection()

    now = datetime.datetime.now()
    cursor = connection.cursor()

    sql = str("""
            INSERT INTO payment (date, total_amt, type, is_completed) VALUES ({0}, {1}, {2}, {3});
        """, now, total_amount, "COD", False)
    
    cursor.execute(sql)
    
    sql = str("""
                SELECT id FROM payment WHERE date = {0}
              """, now)
    
    cursor.execute(sql)
    
    result = cursor.fetchall()
    payment_id = result[0].id

    sql = str("""
                UPDATE orders SET payment_id = {0} WHERE id = {1}
              """, payment_id, order_id)
    
    cursor.execute(sql)

    conn.put_connection(connection)

    return id