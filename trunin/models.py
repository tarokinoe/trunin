from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy import create_engine

import datetime


engine = create_engine('sqlite:///db.sqlite3')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


class Photo(Base):
    __tablename__ = 'photo'
    id = Column(Integer, primary_key=True)
    vk_id = Column("VK photo id ", Integer, unique=True, nullable=False)
    link = Column("link", String(500), nullable=False)
    created_on = Column(
        "Created on",
        DateTime,
        default=datetime.datetime.now,
        nullable=False)
    changed_on = Column(
        "last updated",
        DateTime,
        default=datetime.datetime.now,
        onupdate=datetime.datetime.now,
        nullable=False
        )

    def __repr__(self):
        return "<Photo(id='{}', vk_id='{}')>".format(self.id, self.vk_id)
