import sqlite3
from typing import Tuple, List
from datetime import datetime

def create_connection() -> sqlite3.Connection:
    conn = sqlite3.connect('tasks.db')
    return conn

def create_table() -> None:
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS tasks (
                        id INTEGER PRIMARY KEY,
                        title TEXT NOT NULL,
                        description TEXT,
                        status TEXT NOT NULL,
                        priority TEXT NOT NULL,
                        due_date TEXT,
                        reminder_time TEXT)''')
    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_table()
