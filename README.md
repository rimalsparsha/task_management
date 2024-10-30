# Task Management API

## Overview
The Task Management API is a Django-based application that allows authenticated users to manage their tasks. Users can create, read, update, and delete tasks, as well as mark them as completed. The API also includes filtering and searching capabilities to easily manage tasks.

## Features
- **Authentication**: Only authenticated users can access and manipulate their tasks.
- **CRUD Operations**: Create, retrieve, update, and delete tasks.
- **Task Completion**: Mark tasks as completed.
- **Filtering and Searching**: Filter and search tasks via the API and the Django admin dashboard.
- **Admin Access**: Admins can view, search, and filter all tasks in the Django admin interface.

## Technologies
- Django
- Django Rest Framework (DRF)
- PostgreSQL
- Docker
- Docker Compose
- Django Filter

## Requirements
- Python 3.9 or later
- Docker and Docker Compose

## Setup Instructions

```bash
1. Clone the Repository:

git clone https://github.com/rimalsparsha/task_management.git
cd task_management

2. Set up PostgreSQL Database in settings.py:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DB_NAME'),
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASSWORD'),
        'HOST': os.environ.get('DB_HOST'),
        'PORT': os.environ.get('DB_PORT'),
    }
}


3. Create a .env File:

SECRET_KEY="YOUR_SECRET_KEY"
DEBUG=True  # Set to False in production
DB_NAME=your_database_name
DB_USER=your_database_user
DB_PASSWORD=your_database_password
DB_HOST="db"  # Container name for the database in Docker Compose
DB_PORT="5432"


4. Build and Run the Application with Docker Compose:

docker-compose up --build

5. Running Tests Directly:

python manage.py test

6. Running Tests with Docker Compose:

The test suite runs automatically when starting the application with Docker Compose.