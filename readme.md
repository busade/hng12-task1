# FastAPI Project

This is a simple FastAPI project with a single `/dev` endpoint. The project also includes CORS support and auto-generated documentation.

## Features

- FastAPI-based web application.
- `/dev` endpoint to return developer information.
- Automatically generated Swagger and ReDoc documentation.
- CORS enabled for cross-origin requests.

---

## Prerequisites

Before running this application, ensure you have the following installed:

- Python 3.7+
- `pip` (Python package manager)

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/busade/hng12-task1.git
   cd hng12-task1

2. Create a virtual environment:
    ```bash
    python -m venv env
    source env/scripts/activate  #on cmd env\scripts\activate

3. Install dependencies
    ```bash
    pip install -r requirements.txt


## Usage
1. Run the Application
    ```bash
    fastapi dev main.py
2. Open your browser and navigate to
    Swagger UI: http://127.0.0.1:8000/docs


## Endpoint
The app has only one endpoint /dev and it will return the user information inluding email, current datetime and a GitHub Url

### Example
    ```JSON
    {
  "email": "adesolaisa3@gmail.com",
  "current_datetime": "2025-01-28T12:34:56.789123",
  "github_url": "github.com/busade/hng12-task1"
}

