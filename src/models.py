from sqlalchemy import Column, Integer, String, enumerate, ForeingnKey
from sqlalchemy.ext.declarative import declarative_basefrom
from sqlalchemy.orm import relationship


Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(100))
    firstname = Column(String(100)) 
    lastname = Column (String(100)) 
    email = Column(String(120), nullable=False, unique=True)

    User = relationship('user', backref="post", uselist=False)
    User = relationship('user', backref="follower", uselist=False)
    User = relationship('user', backref="comment", uselist=False)



class Post(Base):
    __tablename__ = 'post'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeingnKey('users.id'), nullable=False)

    post = relationship('post', backref="comment", uselist=False)
    post = relationship('post', backref="media", uselist=False)




class Follower(Base):
    __tablename__ = 'follower'

    user_from_id = Column(Integer, ForeingnKey('users.id'), nullable=False)
    user_to_id = Column(Integer, ForeingnKey('users.id'), nullable=False)




class Comment(Base):
    __tablename__ = 'comment'

    id = Column(Integer, primary_key=True)
    comment_text = Column(String(100))
    author_id = Column(Integer, ForeingnKey('post.id'), nullable=False)
    post_id = Column(Integer, ForeingnKey('post.id'), nullable=False)




class Media(Base):
    __tablename__ = 'media'

    id = Column(Integer, primary_key=True)
    type = Column(enumerate(100))
    url = Column(String(100))
    post_id = Column(Integer, ForeingnKey('post.id'), nullable=False)
