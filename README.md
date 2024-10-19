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
1. Clone repository
`git clone git@github.com:savvlex/shortenurl.git`

2. Install venv
`python3 -m venv venv`

3. Install depencies
`pip install -r requirements.txt`

4. Start app on port 8080 (or any different port)
`uvicorn app.main:app --reload --port 8080`

5. Follow to http://127.0.0.1:8080/docs

6. Use swagger to test


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
