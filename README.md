FastAPI Notepad



A personal productivity application for managing notes, tasks, and schedules with a lightweight AI placeholder for future automation.



1\. Project Overview



FastAPI Notepad is a backend-first productivity application that allows users to securely manage personal notes, tasks, and their history. The project is designed to be modular and expandable, with a placeholder AI module for future integration of text summarization or task recommendations.



Core Philosophy:



Modularity: Backend-first design enables easy addition of features such as AI-assisted task management.



Security: User authentication and authorization using JWT ensures data privacy.



Simplicity: Clean API structure to enable easy frontend integration or Streamlit UI.



2\. Technology Stack

Component	Choice	Purpose / Benefit

Backend	FastAPI (Python)	High-performance API with easy database integration.

Database	SQLite (or SQLAlchemy ORM)	Stores users, tasks, and task history. Easy to switch to PostgreSQL later.

Authentication	OAuth2 + JWT	Secures user data with token-based authentication.

AI Engine	Placeholder (local llm.py)	Placeholder summarization function for future AI integration.

3\. System Workflows

Backend (FastAPI)



Handles all CRUD operations for tasks and notes.



Authenticates users with JWT.



Provides history and calendar endpoints for tasks.



Contains AI placeholder for text summarization (local only, not connected to Hugging Face yet).



Database (SQLite / SQLAlchemy)



Stores users, tasks, completed tasks, and due dates.



Tasks are linked to users via owner\_id.



Completed tasks are timestamped automatically.



AI Placeholder (llm.py)



Function: summarize\_text(text: str) -> str



Returns a simple truncated summary of text.



No external AI integration yet.



4\. Directory Structure \& Key Files

fastapi-notepad/

│

├─ app/

│   ├─ main.py          # API endpoints and task logic

│   ├─ models.py        # Database models (User, Task)

│   ├─ schemas.py       # Pydantic request/response models

│   ├─ auth.py          # Authentication helpers (JWT + password hashing)

│   └─ service/

│       └─ llm.py       # Placeholder LLM module

│

├─ requirements.txt     # Python dependencies

├─ README.md            # Project documentation

├─ notepad.db           # SQLite database

└─ .gitignore



5\. Core Features



User Authentication



Register and login endpoints.



JWT token generation and validation.



Task CRUD



Create, read, update, and delete tasks.



Mark tasks as completed with timestamp tracking.



Task History



Fetch all tasks with filtering by completion.



Tasks sorted by completion status and due date.



Calendar Support



Fetch individual tasks by ID for calendar integration.



LLM Placeholder



Summarizes text using summarize\_text function (local only).



Ready for future AI integration.



6\. Setup \& Running Locally

1\. Backend

cd fastapi-notepad

python -m venv venv

\# Activate environment

\# Windows: .\\venv\\Scripts\\activate

\# Linux/Mac: source venv/bin/activate

pip install -r requirements.txt



uvicorn app.main:app --reload



2\. Testing API



Open Swagger UI: http://127.0.0.1:8000/docs



Test all endpoints:



/register → create user



/login → get JWT token



/tasks → create or fetch tasks



/tasks/history → get completed/pending tasks



/tasks/{id} → fetch or update specific tasks



7\. Usage Guide

Create a Task

POST /tasks

{

&nbsp; "title": "Finish report",

&nbsp; "description": "Complete the end-of-year summary",

&nbsp; "due\_date": "2025-12-31T17:00:00"

}



Fetch Task History

GET /tasks/history

Authorization: Bearer <JWT\_TOKEN>



Summarize Text (AI Placeholder)

from app.service.llm import summarize\_text



text = "This is a very long note that needs summarization."

summary = summarize\_text(text)

print(summary)  # Output: Summary: This is a very long note that needs summarization....



8\. Future Enhancements



Connect LLM module to Hugging Face or OpenAI for real AI summarization.



Implement Streamlit or React frontend.



Add calendar view with interactive task management.



Support multi-user collaborative tasks.



Upgrade database to PostgreSQL or Supabase for production.



9\. Security Considerations



JWT-based authentication.



Passwords hashed with secure algorithms.



.env for secrets (never push to GitHub).

