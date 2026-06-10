
---

#  Project Management CLI Tool

A Python-based Command-Line Interface (CLI) application for managing users, projects, and tasks in a simulated multi-user environment. The system supports structured project tracking, task management, and data persistence using JSON files.

---

##  Features

*  Create and manage users
*  Create projects linked to users
*  Create tasks linked to projects
* Mark tasks as complete
*  Search projects and tasks
*  View a dashboard summary
*  Persistent storage using JSON files
*  Modular architecture (models, services, CLI, storage, utils)
*  Unit testing with pytest
* Clean CLI output using `rich`

---

##  Project Structure

```
project-management-cli/
│
├── main.py
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
└── README.md
```

---

##  Installation

### 1. Clone the repository

```bash
git clone 
cd project-management-cli
```

### 2. Install dependencies (using Pipenv)

```bash
pip install pipenv
pipenv install
pipenv shell
```

---

##  Running the Application

Run the CLI using:

```bash
python main.py <command> [options]
```

---

##  Available Commands

###  User Commands

```bash
add-user --name "Alex" --email "alex@mail.com"
list-users
```

---

### Project Commands

```bash
add-project --user "Alex" --title "CLI Tool"
list-projects --user "Alex"
search-project --keyword "CLI"
```

---

### Task Commands

```bash
add-task --project "CLI Tool" --title "Implement CLI parser"
list-tasks --project "CLI Tool"
complete-task --task "Implement CLI parser"
search-task --keyword "CLI"
```

---

### Dashboard

```bash
dashboard
```

---

## Data Persistence

All data is stored locally in JSON files inside the `data/` folder:

* `users.json`
* `projects.json`
* `tasks.json`

The system automatically loads and saves data using file I/O operations.

---

## Running Tests

Run tests using pytest:

```bash
pytest
```

Tests cover:

* User creation
* Project creation
* Task creation and completion logic

---

## Architecture Overview

The system follows Object-Oriented Programming principles:

* **Models** → Define core entities (User, Project, Task)
* **Services** → Business logic layer
* **CLI Layer** → Handles user input and commands
* **Storage Layer** → Handles JSON file persistence
* **Utils** → Helper functions (ID generation, validation)

Relationships:

* A User has many Projects
* A Project has many Tasks

---

## Key Technologies

* Python 3.14
* argparse (CLI handling)
* JSON (data storage)
* rich (CLI formatting)
* pytest (testing)
* Pipenv (dependency management)

---

## Author

Project developed as part of a Python CLI & Object-Oriented Programming assignment.

---

## License

This project is for educational purposes.

