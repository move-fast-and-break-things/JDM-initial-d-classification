from core.event_handler import EventHandler
from models import Users
from sqlalchemy.future import select
from core.event_types import EventTypes    


class StartGreetings(EventHandler):
    def initate(self):
        self.event_types = [
            EventTypes.MESSAGE
        ]
        self.api_bot = self.depends.api_bot()  

    async def check_event(self, event):
        if event['message'].get('text') == '/start':
            return True
        return False

    async def handle_event(self, event):
        id = event['message']['from']['id']
        async_session = self.depends.async_db_session().async_session

        async with async_session() as session:
            user_be = await session.execute(select(Users).where(Users.user_id == id))
            user_be = user_be.scalars().first()

        if user_be:
            self.api_bot.method('sendMessage',
                                    {'chat_id': event['message']['chat']['id'],
                                     'text': 'Ты меня уже запускал'})
        else:
            with open('img/greetings.jpg', 'rb') as img:
                self.api_bot.method('sendPhoto',
                                {'chat_id': event['message']['chat']['id'],
                                 'caption': 'Привет, ты здесь впервые. 🤗\
                                 Этот бот может классифицировать изображения, на которых присутствуют автомобили из аниме Initial D: \
                                 -Toyota AE86 \n-Nissan Skyline GT R\n-Nissan Sileighty 7\n-Mazda RX-7\n',
                                 }, files = {'photo': img})
            async with async_session() as session:
                user = Users(user_id=id, role='Novice', is_admin=False)
                session.add(user)
                await session.commit()

