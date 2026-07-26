# Backend Learning

A FastAPI-based task management app for learning backend development concepts such as REST APIs, SQLAlchemy, authentication, templates, and database persistence.

## Overview

This project demonstrates how to build a small full-stack-style backend with:
- FastAPI for API routes
- SQLAlchemy for ORM-based database access
- SQLite for local persistence
- JWT-based authentication
- Jinja2 templates for rendering basic HTML pages

## Current Features

- Task CRUD operations (create, read, update, delete)
- User registration and login
- Password hashing with bcrypt
- JWT access token generation
- HTML templates for the landing, login, and registration pages
- Pydantic request validation

## Project Structure

- `main.py` - FastAPI app, routes, and template rendering
- `models.py` - SQLAlchemy database models for tasks and users
- `schemas.py` - Pydantic schemas for task input validation
- `database.py` - Database engine, session factory, and dependency injection
- `auth.py` - Password hashing and JWT token helpers
- `templates/` - HTML files for the frontend views
- `tasks.db` - SQLite database created automatically on startup

## Getting Started

1. Create and activate a virtual environment:
   ```bash
   python -m venv backendlearning
   backendlearning\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install fastapi sqlalchemy python-dotenv pydantic email-validator passlib python-jose jinja2 uvicorn
   ```

3. Run the development server:
   ```bash
   uvicorn main:app --reload
   ```

## API Endpoints

### Tasks
- `GET /` - Renders the home page template
- `POST /task` - Create a new task
- `GET /task` - Get all tasks
- `GET /task/{task_id}` - Get a specific task by ID
- `PUT /task/{task_id}` - Update a task
- `DELETE /task/{task_id}` - Delete a task

### Authentication
- `POST /register` - Register a new user
- `POST /login` - Log in a user and return a JWT access token

## Data Models

### Task
- `id` - Unique integer ID
- `title` - Task title
- `description` - Optional task description
- `completed` - Boolean completion flag

### User
- `id` - Unique integer ID
- `username` - Unique username
- `hashed_password` - Hashed password value

## Notes

- The application uses SQLite, so no separate database server is required.
- The secret key in `auth.py` should be replaced with a stronger value in a real application.

## License

This project is intended for learning and personal use.