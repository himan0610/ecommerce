import multiprocessing
from backend.type import ItemDto
from backend.service.OrderService import saveItem

queue = multiprocessing.Queue()

def enqueue(item:ItemDto, flag):
    queue.put(tuple(item, flag))

def execute():
    while not queue.empty():
        item = queue.get()
        saveItem(item[0], item[1])
        