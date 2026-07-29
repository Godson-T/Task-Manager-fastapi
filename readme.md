# Backend Learning

A FastAPI-based task management app for learning backend development concepts such as REST APIs, SQLAlchemy, authentication, templates, and database persistence.

## Overview

This project demonstrates how to build a small backend with:
- FastAPI for API routes
- SQLAlchemy for ORM-based database access
- SQLite for local persistence
- JWT-based authentication
- Jinja2 templates for a simple home page

## Current Features

- Task CRUD operations (create, read, update, delete)
- User registration and login
- Password hashing with bcrypt
- JWT access token generation
- Basic home page rendered with Jinja2
- Pydantic request validation for task payloads

## Project Structure

- `main.py` - FastAPI app, routes, and template rendering
- `models.py` - SQLAlchemy models for tasks and users
- `schemas.py` - Pydantic schema for task input validation
- `database.py` - Database engine, session factory, and dependency helper
- `auth.py` - Password hashing, JWT creation, and token verification
- `templates/` - HTML files for the frontend views
- `tasks.db` - SQLite database file created automatically on first run

## Getting Started

1. Create and activate a virtual environment:
   ```powershell
   python -m venv backendlearning
   backendlearning\Scripts\activate
   ```

2. Install dependencies:
   ```powershell
   pip install fastapi sqlalchemy pydantic passlib[bcrypt] python-jose jinja2 uvicorn
   ```

3. Run the development server:
   ```powershell
   uvicorn main:app --reload
   ```

## API Endpoints

### Tasks
- `GET /` - Renders the home page template
- `POST /task` - Create a new task (requires `Authorization: Bearer <token>` header)
- `GET /task` - Get all tasks
- `GET /task/{task_id}` - Get a specific task by ID
- `PUT /task/{task_id}` - Update a task
- `DELETE /task/{task_id}` - Delete a task

### Authentication
- `POST /register` - Register a new user with `username` and `password`
- `POST /login` - Log in a user and return a JWT access token

## Authentication Notes

- The `POST /task` route requires a valid JWT access token in the `Authorization` header.
- The token is created by `auth.py` and expires after 24 hours.
- In a production app, replace `SECRET_KEY` in `auth.py` with a secure, environment-driven secret.

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
- The `SECRET_KEY` in `auth.py` should be replaced with a stronger value in a real application.
- The current app stores tasks without user ownership metadata.

## License

This project is intended for learning and personal use.
