from fastapi import FastAPI

app = FastAPI()

import uvicorn
import sqlite3


def run():
    print("sqlite3.threadsafety = " + str(sqlite3.threadsafety))
    print("sqlite3.version_info = " + str(sqlite3.version_info))
    print("sqlite3.sqlite_version_info = " + str(sqlite3.sqlite_version_info))
    # conn = sqlite3.connect(":memory:")
    conn = sqlite3.connect("file:memdb1?mode=memory&cache=shared", check_same_thread=False, uri=True)
    conn.execute('CREATE TABLE tbTest (fld1, fld2)')
    conn.close()
    print("123333333333")


# 至少保证一个链接不关闭，否则内存就释放
conn1 = sqlite3.connect("file:memdb1?mode=memory&cache=shared", check_same_thread=False, uri=True)



@app.get("/sql")
async def sql():
    conn1.execute("INSERT INTO tbTest VALUES ('fld1', 'fld2')")
    conn1.commit()
    tb = list(conn1.execute('select * from tbTest '))
    return tb


@app.get("/sqlback")
async def sqlback():
    conn2 = sqlite3.connect("file:memdb1?mode=memory&cache=shared", check_same_thread=False, uri=True)
    conn2.execute("INSERT INTO tbTest VALUES ('fld3', 'fld4')")
    conn2.commit()
    tb2 = list(conn2.execute('select * from tbTest'))
    conn2.close()
    return tb2


if __name__ == "__main__":
    run()
    uvicorn.run("main:app", host="0.0.0.0", port=5555)
