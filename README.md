
---
#  Project Management CLI Tool

A Python-based Command-Line Interface (CLI) application for managing users, projects, and tasks in a structured multi-user system.

The system demonstrates **Object-Oriented Programming (OOP)**, **file persistence**, **CLI design**, **input validation**, and **unit testing** using modern Python practices.

---

## Features

-  Create and manage users
-  Create projects linked to users
-  Create tasks linked to projects
- Mark tasks as complete
- Search projects and tasks
- Dashboard summary view
- JSON file persistence (local storage)
- Strong OOP design with inheritance (BaseModel)
- Unit testing with pytest
-  Clean CLI output using `rich`
-  Input validation using Pydantic

---

##  Project Structure

```

project-management-cli/
│
├── main.py
│
├── cli/
│   ├── parser.py
│   └── commands.py
│
├── models/
│   ├── base_model.py
│   ├── user.py
│   ├── project.py
│   └── task.py
│
├── services/
│   ├── user_service.py
│   ├── project_service.py
│   ├── task_service.py
│   └── dashboard_service.py
│
├── storage/
│   └── json_db.py
│
├── utils/
│   ├── id_generator.py
│   └── validators.py
│
├── data/
│   ├── users.json
│   ├── projects.json
│   └── tasks.json
│
├── tests/
│   ├── test_users.py
│   ├── test_projects.py
│   └── test_tasks.py
│
├── Pipfile
├── README.md
└── Pipfile.lock

````

---

## Installation

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd project-management-cli
````

---

### 2. Install dependencies (Pipenv)

```bash
pip install pipenv
pipenv install
pipenv shell
```

---

##  Running the Application

Run the CLI tool using:

```bash
python main.py <command> [options]
```

---

## Available Commands

### User Commands

```bash
add-user --name "Ngoyoni" --email "ngoyoni@mail.com"
list-users
```

---

### Project Commands

```bash
add-project --user "Ngoyoni" --title "CLI Tool"
list-projects --user "Ngoyoni"
search-project --keyword "CLI"
```

---

### Task Commands

```bash
add-task --project "CLI Tool" --title "Implement CLI Parser"
list-tasks --project "CLI Tool"
complete-task --task "Implement CLI Parser"
search-task --keyword "CLI"
```

---

###  Dashboard

```bash
dashboard
```

---

##  Data Persistence

All data is stored locally using JSON files:

* `data/users.json`
* `data/projects.json`
* `data/tasks.json`

Data is automatically loaded and saved using a dedicated storage layer.

---

##  Running Tests

Run all tests using:

```bash
pytest
```

### Test Coverage

* User creation & validation
* Project creation & relationships
* Task lifecycle (create → complete)
* OOP inheritance (BaseModel)

---

##  Architecture Overview

The system follows a clean layered architecture:

###  Models

Defines core entities:

* User
* Project
* Task

All models inherit from **BaseModel**, which provides:

* Unique ID generation
* Timestamp tracking
* Shared serialization logic

---

###  Services

Business logic layer:

* UserService
* ProjectService
* TaskService
* DashboardService

---

### CLI Layer

Handles:

* Argument parsing (`argparse`)
* Command routing
* User interaction

---

### Storage Layer

Handles:

* JSON file reading/writing
* Persistent data storage

---

###  Utils

* ID generation
* Input validation (Pydantic)

---

##  Relationships

*  A **User** has many Projects
* A **Project** has many Tasks
* A **Task** belongs to a Project

---

## Technologies Used

* Python 3.12+
* argparse (CLI system)
* JSON (data storage)
* rich (CLI formatting)
* pytest (testing)
* pydantic (validation)
* pipenv (dependency management)

---

## Author

Developed as part of a Python OOP + CLI assignment demonstrating:

* modular architecture
* object-oriented design
* real-world CLI system design

---

## License

This project is for educational purposes only.

