from sqlalchemy import create_engine, select
from sqlalchemy.sql import select
from student import students

engine = create_engine('sqlite:///college.db', echo = True)

conn = engine.connect()
st = students.alias("a")
s = select([st]).where(st.c.id > 2)
print(conn.execute(s).fetchall())

conn.close()