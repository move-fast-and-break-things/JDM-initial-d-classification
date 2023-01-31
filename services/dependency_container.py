from dependency_injector import containers, providers
from services.telegram_api import TelegramApi
from database import DatabaseSession
from services.worker import TaskQueue


class IOCContainer(containers.DeclarativeContainer):

    config = providers.Configuration()

    api_bot = providers.Singleton(
        TelegramApi,
        config.api_bot.token,
    )

    async_db_session = providers.Singleton(
        DatabaseSession,
        config.async_db_session.db_uri,
    )

    task_queue = providers.Singleton(
        TaskQueue,
    )

