from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from create_dbengine import engine

Base = declarative_base()

class Books(Base):
    __tablename__ = 'book'
    id = Column(Integer, print_key=True, nullable=False)
    title = Column(String(50), unique =True)
    author = Column(String(50))
    publisher = Column(String(50))
Base.metadata.create_all(bind=engine)

