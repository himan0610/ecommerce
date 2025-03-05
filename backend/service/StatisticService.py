import backend.service.Connection as conn

def get_statistics():
    connection = conn.get_connection()

    cursor = connection.cursor()

    sql = str("""
            SELECT count(id) as count FROM orders WHERE status_id = 1;
        """, id)
    
    cursor.execute(sql)
    result = cursor.fetchall()
    pending_count = result[0]["count"]

    sql = str("""
            SELECT count(id) as count FROM orders WHERE status_id = 2;
        """, id)
    
    cursor.execute(sql)
    result = cursor.fetchall()
    processing_count = result[0]["count"]

    sql = str("""
            SELECT count(id) as count FROM orders WHERE status_id = 3;
        """, id)
    
    cursor.execute(sql)
    result = cursor.fetchall()
    completed_count = result[0]["count"]

    sql = str("""
            SELECT sum(total_processing_time) as count FROM completed_order_time_series;
        """, id)
    
    cursor.execute(sql)
    result = cursor.fetchall()
    total_processing_time = result[0]["count"]

    sql = str("""
            SELECT sum(total_processing_time)/sum(total_no_of_orders) as count FROM completed_order_time_series;
        """, id)
    
    cursor.execute(sql)
    result = cursor.fetchall()
    avg_processing_time = result[0]["count"]

    result = {
        "total_processing_time": total_processing_time,
        "average_processing_time": avg_processing_time,
        "status_count" : {
            "pending" : pending_count,
            "processing": processing_count,
            "completed": completed_count
        }
    }

    conn.put_connection(connection)

    return result