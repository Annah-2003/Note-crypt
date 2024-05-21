# app.py
from flask import Flask, request, jsonify
import database as db

app = Flask(__name__)

@app.route('/tasks', methods=['GET'])
def get_all_tasks():
    tasks = db.get_tasks()
    return jsonify(tasks)

@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    db.add_task(data['title'], data['description'], data['status'])
    return jsonify({"message": "Task created successfully!"}), 201

@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    data = request.get_json()
    db.update_task(task_id, data['title'], data['description'], data['status'])
    return jsonify({"message": "Task updated successfully!"})

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    db.delete_task(task_id)
    return jsonify({"message": "Task deleted successfully!"})

if __name__ == '__main__':
    app.run(debug=True)
