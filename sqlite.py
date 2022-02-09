import sqlite3

p = sqlite3.connect("file:memDB1?mode=memory&cache=shared", uri=True)

p.execute('CREATE TABLE tbTest (fld1, fld2)')
p.execute("INSERT INTO tbTest VALUES ('fld1', 'fld2')")

p.commit()

tb = list(p.execute('select * from tbTest '))
print(tb)

q = sqlite3.connect("file:memDB1?mode=memory&cache=shared", uri=True)
q.execute("INSERT INTO tbTest VALUES ('fld3', 'fld4')")
q.commit()

tb2 = list(q.execute('select * from tbTest '))
print(tb2)
