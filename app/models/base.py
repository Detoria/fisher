from sqlalchemy import Column, Integer, String, SmallInteger
from flask_sqlalchemy import SQLAlchemy  ##  pipenv install flask_sqlalchemy


db = SQLAlchemy()

class Base(db.Model):
    # create_time = Column('create_time', Integer)
    status = Column(SmallInteger, default=1)