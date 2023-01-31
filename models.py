from app import Base
from sqlalchemy.orm import backref, relationship
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean

class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key = True, autoincrement = True)
    user_id = Column(Integer)
    role = Column(String(50))
    is_admin = Column(Boolean)

    def __repr__(self):
        return f'<User {self.user_id}>'
