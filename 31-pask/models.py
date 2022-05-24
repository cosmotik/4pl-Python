from database import Base
from sqlalchemy import Column, String, Integer, ForeignKey, Boolean
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True)

    posts = relationship("Post", back_populates='owner')


class PostSettings(Base):
    __tablename__ = 'settings'

    id = Column(Integer, primary_key=True, index=True)
    is_active = Column(Boolean, default=False)

    post = relationship('Post', back_populates='settings', uselist=False)


class Post(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    body = Column(String)

    owner_id = Column(Integer, ForeignKey('users.id'))
    owner = relationship('User', back_populates='posts')

    settings_id = Column(Integer, ForeignKey('settings.id'))
    settings = relationship('PostSettings', back_populates='post')
