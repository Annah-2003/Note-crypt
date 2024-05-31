# Note-crypt by Irene Gitau

# Description

 This Task Manager Application is a web-based tool for managing tasks with features such as task reminders, prioritization, and sorting. It is built using Flask, SQLite, and Flask-Mail.

# Features
 * Create, read, update, and delete tasks.
 * Set reminders for tasks and receive email       notifications.
 * Prioritize tasks and sort by priority or due date.

# Requirements
 * Python 3.x
 * Flask
 * Flask-Mail
 * APScheduler
 * SQLite
 * Postman (for testing API endpoints)


# Installation
## Step 1: Clone the Repository
 git clone https://github.com/Annah-2003/ 
 cd task-manager

## Step 2: Set Up a Virtual Environment
 python -m venv venv
 source venv/bin/activate  # On Windows use `venv\Scripts\activate`

## Step 3: Install Dependencies
 pip install flask flask-mail apscheduler

## Step 4: Configure Flask-Mail
 Edit app.py to include your email credentials.

 `app.config['MAIL_SERVER'] = 'smtp.example.com'`
 `app.config['MAIL_PORT'] = 587`
 `app.config['MAIL_USE_TLS'] = True`
 `app.config['MAIL_USERNAME'] = 'your-email@student.com'`
 `app.config['MAIL_PASSWORD'] = 'your-email-password'`

## Database Setup

## Step 5: Create the Database and Table
 Create a file named models.py
 Run the script to create the database and table:  python models.py

# Application Code

## Step 6: Create the Database Operations File
 Create a file named database.py

## Step 7: Create the Flask Application
 * Create a file named app.py

# Running the Application

## Step 8: Start the Flask Server
 * python app.py

## Step 9: View and Test the Application
 Open your web browser and navigate to http://127.0.0.1:5000. You can use tools like Postman to interact with the API.

 API Endpoints
 GET /tasks: Retrieve all tasks.
 POST /tasks: Create a new task.

Happy Coding!!