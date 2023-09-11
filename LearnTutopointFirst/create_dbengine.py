from sqlalchemy import create_engine
from sqlalchemy.dialects.sqlite import *
DB_URL = "sqlite:///./test.db"
engine = create_engine(DB_URL, connect_args={"check_same_thread" : False})
 