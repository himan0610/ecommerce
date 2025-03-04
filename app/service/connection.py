import psycopg2
from psycopg2 import pool

# Create a connection pool
connection_pool = psycopg2.pool.SimpleConnectionPool(
    1,      # minimum number of connections
    10,     # maximum number of connections
    user="postgres",
    password="root",
    host="localhost",
    port="5432",
    database="ecommerce"
)

def get_connection():
    connection = connection_pool.getconn()
    return connection

def put_connection(connection):
    connection_pool.putconn(connection)
    