from sqlalchemy import create_engine, select, text, String
from sqlalchemy.sql import text, bindparam, and_

engine = create_engine('sqlite:///college.db', echo = True)

conn = engine.connect()

t = text("SELECT * FROM students limit 1")
result = conn.execute(t)
for row in result:
    print(row)

s = text("SELECT students.name, students.lastname FROM students WHERE students.name between :x and :y")
print(conn.execute(s, x='A', y='L').fetchall())

s = select([text("students.name, students.lastname from students")]).where(text("students.name between :x and :y"))
print(conn.execute(s, x = 'A', y = 'L').fetchall())

s2 = select([text("students.id, students.name from students")]).where(
   and_( text("students.name between :x and :y"),
         text("students.id > 10"))
   )
print(conn.execute(s2, x = 'A', y = 'L').fetchall())

stmt = text("SELECT * FROM students WHERE students.name BETWEEN :x AND :y")

stmt = stmt.bindparams(
   bindparam("x", type_= String), 
   bindparam("y", type_= String)
)

result = conn.execute(stmt, {"x": "A", "y": "L"})
for row in result:
    print(row)

conn.close()