from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession


class DatabaseSession():
    def __init__(self, db_uri):
        self.engine = create_async_engine(db_uri, future=True, echo=True)
        self.async_session = sessionmaker(self.engine, expire_on_commit=False, class_=AsyncSession)
