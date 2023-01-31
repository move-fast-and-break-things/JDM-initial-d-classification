from app import depends
from core.event_controler import EventControler
from handlers_list import handlers_list
import asyncio
from threading import Thread


controler= EventControler(handlers_list, depends)
loop = asyncio.new_event_loop()


def f(loop):
    asyncio.set_event_loop(loop)
    loop.run_forever()


t = Thread(target=f, args=(loop,))
t.setDaemon(True)


def send_update(data):
    loop.call_soon_threadsafe(lambda:asyncio.ensure_future(controler.processing(data), loop=loop))


def app_start():
    last_id = 0
    while True:
        api = depends.api_bot()

        updates = api.method('getUpdates', {'timeout': 5, 'offset': last_id})
        
        if updates['ok']:
            for update in updates['result']:
                last_id = update['update_id'] + 1
                send_update(update)
