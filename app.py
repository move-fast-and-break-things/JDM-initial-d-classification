from config import BaseConfig, TelegramConfig
from sqlalchemy.orm import declarative_base
from services.dependency_container import IOCContainer


Base = declarative_base()

depends = IOCContainer()

depends_config = {
    'api_bot': {
        'token': TelegramConfig.TOKEN,
    },
    'async_db_session': {
        'db_uri': BaseConfig.SQLALCHEMY_DATABASE_URI,
    }
}

depends.config.from_dict(depends_config)
