import psycopg2
from psycopg2 import pool
import configparser

config = configparser.ConfigParser()
config.read('../config.properties')

db_host = config['Backend']['DB_HOST']
db_user = config['Backend']['DB_USER_NAME']
db_password = config['Backend']['DB_PASSWORD']
db_port = config['Backend']['DB_PORT']
db_name = config['Backend']['DB_NAME']

# Create a connection pool
connection_pool = psycopg2.pool.SimpleConnectionPool(
    1,
    10,
    user=db_user,
    password=db_password,
    host=db_host,
    port=db_port,
    database=db_name
)

def get_connection():
    connection = connection_pool.getconn()
    return connection

def put_connection(connection):
    connection_pool.putconn(connection)
    