from backend.type import ItemDto
from backend.service.OrderService import saveItem
import asyncio

queue = asyncio.Queue(maxsize=1000)

async def enqueue(item:ItemDto, flag):
    await queue.put(tuple(item, flag))

async def execute():
    while not queue.empty():
        item = await queue.get()
        saveItem(item[0], item[1])

asyncio.run(execute())
        