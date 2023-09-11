from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, select
engine = create_engine('sqlite:///college.db', echo = True)
meta = MetaData()

students = Table(
   'students', meta, 
   Column('id', Integer, primary_key = True), 
   Column('name', String), 
   Column('lastname', String),
)

conn = engine.connect()
s = students.select().where(students.c.id>2)
result = conn.execute(s)
for row in result:
    print(row)

s1 = select([students])
result = conn.execute(s1)
print(result.fetchone())

conn.close()