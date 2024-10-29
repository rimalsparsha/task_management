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

### 1. Clone the Repository
```bash
git clone https://github.com/rimalsparsha/task_management.git
cd task_management

### 2. Create a .env File
    SECRET_KEY="YOUR_SECRET_KEY"
    DEBUG="YOUR_DEBUG"
    DB_NAME=your_database_name
    DB_USER=your_database_user
    DB_PASSWORD=your_database_password

### 3. Build and Run the Application
    docker-compose up --build
