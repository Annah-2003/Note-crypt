# models.py
import sqlite3

def create_connection():
    conn = sqlite3.connect('tasks.db')
    return conn

def create_table():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS tasks (
                        id INTEGER PRIMARY KEY,
                        title TEXT NOT NULL,
                        description TEXT,
                        status TEXT NOT NULL)''')
    conn.commit()
    conn.close()

create_table()
