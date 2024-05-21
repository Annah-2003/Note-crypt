import sqlite3
from models import create_connection

def add_task(title, description, status, priority, due_date, reminder_time):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tasks (title, description, status, priority, due_date, reminder_time) VALUES (?, ?, ?, ?, ?, ?)", 
                   (title, description, status, priority, due_date, reminder_time))
    conn.commit()
    conn.close()

def get_tasks():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()
    conn.close()
    return tasks

def update_task(task_id, title, description, status, priority, due_date, reminder_time):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE tasks SET title = ?, description = ?, status = ?, priority = ?, due_date = ?, reminder_time = ? WHERE id = ?", 
                   (title, description, status, priority, due_date, reminder_time, task_id))
    conn.commit()
    conn.close()

def delete_task(task_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()
