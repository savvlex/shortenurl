# URL Shorter API


## Description
Simple servise that allows to create short links for URLs. Also allows redirections to original URLs by short.


## Technologies
- python 3.11.0
- FastAPI
- Pydantic
- Alembic
- aiosqlite
- uvicorn


## Installation and Usage
Clone repository

`git clone git@github.com:savvlex/shortenurl.git`

Install venv

`python3 -m venv venv`

Install depencies

`pip install -r requirements.txt`

Start app on port 8080 (or any different port)

`uvicorn app.main:app --reload --port 8080`

Follow to http://127.0.0.1:8080/docs

Use swagger to test


## Srtucture
This project follows a modular architecture to ensure clean separation of concerns, maintainability, and scalability. Below is a breakdown of the directory structure:

- **`api/`**  
  Contains route handlers that define API endpoints (e.g., `urls.py`).

- **`core/`**  
  Manages core configurations such as database setup (`db.py`) and application settings (`config.py`).

- **`crud/`**  
  Implements database operations (Create, Read, Update, Delete) for the application models (e.g., `urls.py`).

- **`models/`**  
  Defines database schemas and ORM models (e.g., `urls.py`).

- **`schemas/`**  
  Provides Pydantic schemas for data validation and serialization (e.g., `urls.py`).

- **`services/`**  
  Contains utility functions and helper logic (e.g., `utils.py`).


## Endpoints

### POST /
Create a short URL.

- **Response**: 201 Created  
- **Request Body**:
```json
{
  "url": "https://example.com"
}
```
- **Response Example**:
```json
{
  "url": "https://example.com",
  "short": "abc123"
}
```

### GET /{short}
Redirect to the original URL.

- **Response**: 307 Temporary Redirect  
- **Path Parameter**:
  - `short`: The shortened URL identifier (e.g., `abc123`).

- **Example**:  
  Request:
  ```
  GET /abc123
  ```

  Response: Redirects to `https://example.com`
