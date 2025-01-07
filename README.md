

# # Django Task Management Project

## Description
This is a Django-based task management application that allows users to manage their tasks. Users can create, update, delete, and mark tasks as completed. The application also supports email reminders for tasks, sending an immediate reminder upon task creation and another reminder one day before the task deadline.

## Features
- Add new tasks with a deadline and optional email reminder
- Mark tasks as completed
- Delete tasks
- Send immediate email reminders upon task creation
- Send email reminders one day before the task deadline
- Task status update without page refresh using AJAX
- User-friendly admin panel with task management features

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/task_management_project.git
    cd task_management_project
    ```

2. **Set up a virtual environment:**
    ```bash
    pipenv install
    ```

3. **Activate the virtual environment:**
    ```bash
    pipenv shell
    ```

4. **Install the required dependencies:**
    ```bash
    pipenv install -r requirements.txt
    ```

5. **Apply the database migrations:**
    ```bash
    python manage.py migrate
    ```

6. **Create a superuser for the admin panel:**
    ```bash
    python manage.py createsuperuser
    ```

7. **Run the development server:**
    ```bash
    python manage.py runserver
    ```

## Used Technologies
- **Django:**  
- **SQLLite:** 
- **HTML/CSS**
- **AJAX**



