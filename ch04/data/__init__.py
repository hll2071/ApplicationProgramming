#db 연결
from typing import Optional
from sqlite3 import Connection, Cursor, connect

conn : Optional[Connection] = None
cur : Optional[Cursor] = None



def get_db():
    global conn,cur
    if conn is None:
        print("connection")
        conn = connect("mydb.db")
        cur = conn.cursor()

get_db()