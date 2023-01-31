import os 

app_dir = os.path.abspath(os.path.dirname(__file__))

class BaseConfig():
    SECRET_KEY = os.environ.get('JDM_SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('JDM_SQLALCHEMY_DATABASE_URI', 'sqlite+aiosqlite:///bot.db')


class TelegramConfig():
    TOKEN = os.environ.get('JDM_BOT_TOKEN', '5801206622:AAEZugaxlaXwn8FkvsUEjF64vh5r_sVC6GU')
