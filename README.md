
---
# Project Management CLI Tool

A powerful Python-based Command Line Interface (CLI) application for managing users, projects, and tasks in a multi-user environment.

The application demonstrates real-world software engineering concepts including:

- Object-Oriented Programming (OOP)
- Service Layer Architecture
- JSON Data Persistence
- Pydantic Validation
- Many-to-Many Relationships/One-to-Many Relationships
- Rich Terminal Interfaces
- Automated Testing with Pytest

---

# Features

## User Management

Create and manage users in the system.

### Supported Commands

- Add User
- List Users
- Edit User
- Delete User

Example:

```bash
python main.py user add --name Ngoyoni --email ngoyoni@mail.com
python main.py user list
python main.py user edit --name Ngoyoni --new-name Brian
python main.py user delete --name Brian
````

---

## Project Management

Projects are owned by users.

### Supported Commands

* Create Project
* List Projects
* Search Projects
* Edit Project
* Delete Project

Example:

```bash
python main.py project add --user Ngoyoni --title "AI System"
python main.py project list
python main.py project search --keyword "AI"
python main.py project edit --title "AI System" --new-title "AI Platform"
python main.py project delete --title "AI Platform"
```

---

## Task Management

Tasks belong to projects and support multiple contributors.

### Features

* Create Tasks
* Edit Tasks
* Delete Tasks
* Search Tasks
* Complete Tasks
* Assign Due Dates
* Track Task Urgency
* Multiple Contributors (Many-to-Many)
* Contributor Management

---

## Create Task

```bash
python main.py task add --project "AI System" --title "Build API"
```

With due date:

```bash
python main.py task add --project "AI System" --title "Train Model" --due 2026-06-13
```

---

## List Tasks

```bash
python main.py task list
python main.py task list --project "AI System"
python main.py task list --completed
python main.py task list --pending
python main.py task list --overdue
python main.py task list --due-soon
python main.py task list --assigned Ngoyoni
```

---

## Search Tasks

```bash
python main.py task search --keyword "Model"
```

---

## Complete Task

```bash
python main.py task complete --title "Build API"
```

---

## Edit Task

```bash
python main.py task edit --title "Build API" --new-title "Backend API"
python main.py task edit --title "Train Model" --due 2026-06-13
python main.py task edit --title "Train Model" --assign Ngoyoni
```

---

## Add Contributor (Many-to-Many)

```bash
python main.py task add-contributor --title "Train Model" --user Ngoyoni
python main.py task add-contributor --title "Train Model" --user Brian
python main.py task add-contributor --title "Train Model" --user Ray
```

Example Result:

```
Train Model
├── Ngoyoni
├── Brian
└── Ray
```

---

## Delete Task

```bash
python main.py task delete --title "Build API"
```

---

# Dashboard

The dashboard provides system-wide analytics.

```bash
python main.py dashboard
```

## Dashboard Includes:

* Total Users
* Total Projects
* Total Tasks
* Completed Tasks
* Productivity Score
* User Overview
* Project Overview
* Smart Task View

Example:

```
PROJECT MANAGEMENT DASHBOARD

Users: 3
Projects: 1
Tasks: 4
Completed: 1
Productivity: 25%
```

---

# Task Urgency System

Tasks are automatically categorized:

| Status   | Meaning       |
| -------- | ------------- |
| Overdue  | Past due date |
| Due Soon | Within 3 days |
| Normal   | Safe timeline |

Example:

```
Train Model
Due Date: 2026-06-13
Urgency: due soon
```

---

# Weekly Report Export

Generate analytics report:

```python
from services.dashboard_service import DashboardService

DashboardService().export_weekly_report()
```

Output file:

```
weekly_report.json
```

Includes:

* Total tasks
* Completed tasks
* Pending tasks
* Overdue tasks
* Full task snapshot

---

# Data Persistence

All data is stored locally using JSON files:

```
data/
├── users.json
├── projects.json
├── tasks.json
└── task_users.json
```

Data persists between runs.

---

# Project Structure

```
project-management-cli/
│
├── main.py
├── cli/
├── models/
├── schemas/
├── services/
├── storage/
├── utils/
├── data/
└── tests/
```

---

# Installation

## Clone Repository

```bash
git clone https://github.com/brianngoyoni-254/-Python-Project-Management-CLI-Tool-.git
cd -Python-Project-Management-CLI-Tool-
```

## Install Dependencies

```bash
pip install pipenv
pipenv install
pipenv shell
```

## Install Packages

```bash
pipenv install rich
pipenv install "pydantic[email]"
```

---

# Running the Application

```bash
python main.py
```

Example:

```bash
python main.py user add --name Ngoyoni --email ngoyoni@mail.com
```

---

# Testing

Run tests:

```bash
pytest
```

Result:

```
11 passed
```

Coverage:

* User lifecycle
* Project lifecycle
* Task lifecycle
* Relationships
* Dashboard logic
* Persistence layer

---

# Technologies Used

* Python 3.12+
* argparse
* rich
* pydantic
* pytest
* pipenv
* JSON storage

---

# Architecture

```
CLI Layer
   ↓
Command Layer
   ↓
Service Layer
   ↓
Model Layer
   ↓
Storage Layer
```

Benefits:

* Clean separation of concerns
* Easy testing
* Scalable structure
* Maintainable logic

---

# Relationships

* User → Projects (1-to-many)
* Project → Tasks (1-to-many)
* User ↔ Tasks (many-to-many)

---

# Author

**Ngoyoni**

Software  Developer

GitHub:
[https://github.com/brianngoyoni-254](https://github.com/brianngoyoni-254)

---

# License

This project is for educational and portfolio use only.

