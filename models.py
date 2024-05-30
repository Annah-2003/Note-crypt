import sqlite3

def create_connection():
    return sqlite3.connect('tasks.db')

def create_table():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        description TEXT,
        status TEXT,
        priority INTEGER,
        due_date TEXT,
        reminder_time TEXT
    )
    ''')
    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_table()
