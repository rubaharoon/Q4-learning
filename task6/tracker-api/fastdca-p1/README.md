# 📝 Task Tracker API

A FastAPI-powered application to manage **Users** and their **Tasks**, built using Pydantic for data validation and in-memory storage.

## 🚀 Features

- ✅ Create and retrieve users
- ✅ Create, retrieve, and update tasks
- ✅ Assign tasks to specific users
- ✅ Validate input using Pydantic (e.g., email, username length, due dates)
- ✅ In-memory storage using Python dictionaries

## 📦 Requirements

- Python 3.9+
- FastAPI
- Uvicorn
- Pydantic `< 2.0`


## 🔧 Installation

1. **Clone the repository**

git clone https://github.com/your-username/task-tracker-api.git
cd task-tracker-api
Create and activate a virtual environment 
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
Install dependencies
pip install fastapi uvicorn "pydantic<2"
▶️ Run the API

uvicorn main:app --reload

📬 API Endpoints
👤 Users
POST /users/ – Create a new user
✅ Validates email and username length

GET /users/{user_id} – Retrieve a user by ID

GET /users/{user_id}/tasks – List all tasks for a specific user

✅ Tasks
POST /tasks/ – Create a task
✅ Validates due date (must be today or future)

GET /tasks/{task_id} – Get task by ID

PUT /tasks/{task_id} – Update task status
✅ Only allows pending, in_progress, or completed

🧠 Pydantic Validations
username: Must be 3–20 characters

email: Must be a valid email address

due_date: Must be today or in the future

status: Must be one of pending, in_progress, completed

🗃️ Data Storage
This project uses in-memory Python dictionaries for storage:
USERS: dict[int, UserRead] = {}
TASKS: dict[int, Task] = {}
⚠️ All data is lost when the server restarts.