import os
import sqlite3


def connection():
    print("Bağlantı yapılıyor..")
    conn = None
    try:
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(BASE_DIR, "database.db")
        with sqlite3.connect(db_path) as db:
            conn = db
            return conn
    except Exception as e:
        print(e)
    return conn
