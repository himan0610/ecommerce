import connection as conn

# Get a connection from the pool
connection = conn.get_connection()

# Use the connection
cursor = connection.cursor()
cursor.execute("SELECT * FROM order_status")
result = cursor.fetchall()

print(result);
# Return the connection to the pool
conn.put_connection(connection)