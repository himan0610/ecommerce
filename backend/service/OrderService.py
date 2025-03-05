import backend.service.Connection as conn
from backend.type import ItemDto
from backend.processor import OrderQueueProcessor
import datetime
from backend.service import PaymentService

def create(items:ItemDto):
    products = items["products"]

    connection = conn.get_connection()

    cursor = connection.cursor()
    flag = True
    for product in products:
        sql = str("SELECT EXISTS(SELECT 1 FROM product WHERE id = {0} AND vendor_id = {1} AND qty_in_stock >= {2})", product["id"], product["vendor_id"], product["quantity"])
        cursor.execute(sql)
        result = cursor.fetchall()
        if result != True:
            flag = False
            
    OrderQueueProcessor.enqueue(items, flag)
    OrderQueueProcessor.execute()
    conn.put_connection(connection)

async def saveItem(items: ItemDto, flag: bool):
    
    connection = conn.get_connection()

    cursor = connection.cursor()
    now = datetime.datetime.now()

    status_id = 2
    if flag == False:
        status_id = 1

    sql = str("""
            INSERT INTO orders (customer_id, status_id, order_date) VALUES ({0}, {1}, {2});
        """, items["customer_id"], status_id, now)
    
    cursor.execute(sql)

    sql = str("""
                SELECT id FROM orders WHERE customer_id = {0} AND order_date = {1}
              """, items["customer_id"], now)
    
    cursor.execute(sql)
    
    result = cursor.fetchall()
    order_id = result[0].id

    total_amount = 0
    
    for product in items["products"]:
        total_amount = total_amount + (product["quantity"] * product["price"])
        sql = str("""
                INSERT INTO order_products 
                    SELECT {0} as order_id, p.id as product_id, {2} as quantity, p.price as price 
                        FROM product p WHERE p.id = {3}
              """, order_id, product["quantity"], product["id"])
        cursor.execute(sql)

    PaymentService.create(order_id, total_amount)
    print("Order have been placed successfully")

    conn.put_connection(connection)

def getById(id):
    connection = conn.get_connection()

    cursor = connection.cursor()

    sql = str("""
            SELECT o.id, o.order_date, o.shipping_date, os.status, op.product_id, op.quantity, op.price, p.total_amount 
            FROM orders o
                JOIN order_status os ON os.id = o.status_id
                JOIN order_product op ON o.id = op.order_id
                JOIN payment p ON p.id = o.payment_id
            WHERE o.id = {0};
        """, id)
    
    cursor.execute(sql)
    result = cursor.fetchall()
    conn.put_connection(connection)
    
    return result
