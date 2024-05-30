import sqlite3
from flask import Flask, request, jsonify
from flask_mail import Mail, Message
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
import database as db

app = Flask(__name__)

# Configurations for Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.example.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'your-email@example.com'
app.config['MAIL_PASSWORD'] = 'your-email-password'
mail = Mail(app)

# Function to send reminder emails
def send_reminder(task):
    with app.app_context():
        msg = Message('Task Reminder', sender='your-email@example.com', recipients=['recipient@example.com'])
        msg.body = f"Reminder: {task[0]} - {task[1]}"
        mail.send(msg)

# Scheduler for reminders
scheduler = BackgroundScheduler()
scheduler.start()

@app.route('/tasks', methods=['GET'])
def get_all_tasks():
    tasks = db.get_tasks()
    return jsonify(tasks)

@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    db.add_task(data['title'], data['description'], data['status'], data['priority'], data['due_date'], data['reminder_time'])
    if data['reminder_time']:
        reminder_time = datetime.strptime(data['reminder_time'], '%Y-%m-%d %H:%M:%S')
        scheduler.add_job(send_reminder, 'date', run_date=reminder_time, args=[[data['title'], data['description']]])
    return jsonify({"message": "Task created successfully!"}), 201

@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    data = request.get_json()
    db.update_task(task_id, data['title'], data['description'], data['status'], data['priority'], data['due_date'], data['reminder_time'])
    return jsonify({"message": "Task updated successfully!"})

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    db.delete_task(task_id)
    return jsonify({"message": "Task deleted successfully!"})

@app.route('/tasks/sorted/priority', methods=['GET'])
def get_tasks_by_priority():
    tasks = db.get_tasks_sorted_by_priority()
    return jsonify(tasks)

@app.route('/tasks/sorted/due_date', methods=['GET'])
def get_tasks_by_due_date():
    tasks = db.get_tasks_sorted_by_due_date()
    return jsonify(tasks)

if __name__ == '__main__':
    app.run(debug=True)
