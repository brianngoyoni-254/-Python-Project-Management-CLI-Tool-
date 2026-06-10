
---

#  Project Management CLI Tool

A Python-based Command-Line Interface (CLI) application for managing users, projects, and tasks in a structured multi-user system.

The system demonstrates **Object-Oriented Programming (OOP)**, **service-layer architecture**, **file-based persistence (JSON)**, **input validation**, and **unit testing with pytest**.

---

##  Features

*  Create and manage users
* Create projects linked to users
*  Create tasks linked to projects
* Mark tasks as complete
*  Search projects and tasks
*  Dashboard-style summaries (optional module)
*  JSON file persistence (local storage)
*  Strong OOP design using `BaseModel`
*  Unit testing with `pytest`
*  Clean CLI output using `rich`
*  Input validation using lightweight validators (Pydantic-based where applicable)

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
│   ├── test_tasks.py
│   └── test_relationships.py
│
├── Pipfile
├── Pipfile.lock
└── README.md
```

---

##  Installation

### 1. Clone the repository

```bash
git clone 
cd project-management-cli
```

---

### 2. Install dependencies (Pipenv)

```bash
pip install pipenv
pipenv install
pipenv shell
```

---

## Running the Application

Run the CLI tool using:

```bash
python main.py <command> [options]
```

Example:

```bash
python main.py add-user --name "Ngoyoni" --email "ngoyoni@mail.com"
```

---

## Available Commands

###  User Commands

```bash
add-user --name "Ngoyoni" --email "ngoyoni@mail.com"
list-users
```

---

###  Project Commands

```bash
add-project --user "Ngoyoni" --title "CLI Tool"
list-projects --user "Ngoyoni"
search-project --keyword "CLI"
```

---

###  Task Commands

```bash
add-task --project "CLI Tool" --title "Implement CLI Parser"
list-tasks --project "CLI Tool"
complete-task --task "Implement CLI Parser"
search-task --keyword "CLI"
```

---

### Dashboard

```bash
dashboard
```

---

##  Data Persistence

All application data is stored locally using JSON files:

* `data/users.json`
* `data/projects.json`
* `data/tasks.json`

A lightweight storage layer handles all read/write operations.

---

##  Running Tests

Run all unit tests:

```bash
pytest
```

###  Test Coverage

* User creation & validation
* Project creation & user linking
* Task lifecycle (create → complete)
* Cross-entity relationships
* BaseModel inheritance checks
* JSON persistence integrity

---

##  Architecture Overview

The system follows a clean layered architecture:

---

###  Models Layer

Defines core entities:

* User
* Project
* Task

All models inherit from:

* `BaseModel` (provides ID + timestamps + serialization)

---

###  Services Layer

Business logic lives here:

* UserService
* ProjectService
* TaskService
* DashboardService

This layer handles:

* validation
* relationships
* persistence
* business rules

---

###  CLI Layer

Handles:

* argument parsing (`argparse`)
* command routing
* user input handling

---

### Storage Layer

Responsible for:

* reading JSON files
* writing JSON files
* maintaining persistent state

---

###  Utils Layer

Utility helpers:

* ID generation
* validation logic (email + user validation)

---

##  Relationships

The system enforces clear relationships:

* A **User** has many Projects
* A **Project** belongs to a User
* A **Task** belongs to a Project

---

##  Technologies Used

* Python 3.14
* argparse (CLI framework)
* JSON (data storage)
* rich (terminal UI formatting)
* pytest (unit testing)
* pydantic (validation layer)
* pipenv (dependency management)

---

## Author

Developed as part of a Python OOP + CLI project demonstrating:

* modular architecture
* service-layer design
* real-world CLI application structure
* test-driven development (TDD-style refinement)

---

## License

This project is for educational purposes only.

---
