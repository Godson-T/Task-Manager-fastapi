# Backend Learning

A FastAPI-based task management system demonstrating backend development concepts including API design, database interaction, and CRUD operations.

## Overview

This project demonstrates building a RESTful API with FastAPI and SQLAlchemy, featuring task management endpoints with full CRUD functionality and database persistence.

## Features

- FastAPI framework for modern Python APIs
- SQLAlchemy ORM for database operations
- Task CRUD operations (Create, Read, Update, Delete)
- Pydantic schemas for request/response validation
- Health check endpoint
- Error handling with HTTP exceptions

## Getting Started

1. Clone the repository
2. Create and activate virtual environment:
   ```bash
   python -m venv backendlearning
   backendlearning\Scripts\activate
   ```
3. Install dependencies
4. Run the development server with: `uvicorn main:app --reload`

## Installation

```bash
pip install fastapi sqlalchemy python-dotenv pydantic email-validator
```

## API Endpoints

- `GET /` - Root endpoint
- `GET /health` - Health check
- `POST /task` - Create a new task
- `GET /task` - Get all tasks
- `GET /task/{task_id}` - Get a specific task by ID

## Project Structure

- `main.py` - FastAPI application and endpoint definitions
- `models.py` - SQLAlchemy database models
- `schemas.py` - Pydantic schemas for request/response validation
- `database.py` - Database configuration and session management
- `backendlearning/` - Virtual environment directory

## Task Model

Tasks include:
- `id` - Unique identifier
- `title` - Task title
- `description` - Task description
- `completed` - Completion status

## Contributing

Contributions are welcome. Feel free to add new endpoints, improve database models, or enhance documentation.

## License

This project is intended for learning and personal use.