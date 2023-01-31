from core.event_handler import EventHandler
from core.event_types import EventTypes

from services.image_classification import classificate
from config import TelegramConfig


class ClassificationImages(EventHandler):
    def initate(self):
        self.event_types = [
            EventTypes.MESSAGE
        ]
        self.api_bot = self.depends.api_bot()  
        self.task_queue = self.depends.task_queue()

    async def check_event(self, event):
        if 'photo' in event['message'].keys():
            return True
        return False

    async def handle_event(self, event):
        id = event['message']['from']['id']
        
        result = self.api_bot.method('sendMessage', {'chat_id': id,\
                            'reply_to_message_id': event['message']['message_id'],
                            'text': 'Принял в обработку 🤔'})

        image = self.api_bot.method('getFile', {'file_id': event['message']['photo'][-1]['file_id']})
        img_path = f'https://api.telegram.org/file/bot{TelegramConfig.TOKEN}/{image["result"]["file_path"]}'
        predict = await self.task_queue.task_delay(
            classificate,
            args=[img_path],
        )
        
        self.api_bot.method('editMessageText', {'message_id': result['result']['message_id'], 'chat_id': result['result']['chat']['id'],\
                            'text': f'Возможно это {predict} 🧐'})
