# database.py
import sqlite3
from typing import List, Tuple  # Add Tuple import

from models import create_connection

def add_task(title: str, description: str, status: str) -> None:
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tasks (title, description, status) VALUES (?, ?, ?)", (title, description, status))
    conn.commit()
    conn.close()

def get_tasks() -> List[Tuple]:
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()
    conn.close()
    return tasks

def update_task(task_id: int, title: str, description: str, status: str) -> None:
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE tasks SET title = ?, description = ?, status = ? WHERE id = ?", (title, description, status, task_id))
    conn.commit()
    conn.close()

def delete_task(task_id: int) -> None:
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()
