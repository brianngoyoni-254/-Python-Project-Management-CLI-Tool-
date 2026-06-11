#  Project Management CLI Tool

A **Python-based Command-Line Interface (CLI) application** for managing users, projects, and tasks in a structured multi-user environment.

The project demonstrates **Object-Oriented Programming (OOP)**, **service-layer architecture**, **file-based persistence (JSON)**, **data relationships**, **input validation**, and **unit testing with `pytest`**.

It is designed as a **real-world simulation of a lightweight project management system**.

---

##  Features

### User Management

* Create users
* List users
* (Optional extension-ready: edit/delete users)

###  Project Management

* Create projects assigned to users
* List projects per user
* Search projects by keyword
* (Optional extension-ready: edit/delete projects)

### Task Management

* Create tasks linked to projects
* Assign tasks automatically via project-user relationship
* Mark tasks as complete
* Smart filtering:

  * Overdue tasks
  * Due soon tasks (≤ 3 days)
  * Completed / pending tasks
  * Assigned user filtering
* (Optional extension-ready: edit/delete tasks)

###  Dashboard

* System-wide analytics overview
* Task urgency classification:

  *  Overdue
  *  Due soon
  * Normal
* Productivity score tracking
* Summary of users, projects, and tasks

### Data Persistence

* Local JSON file storage
* Automatic load/save layer abstraction
* Persistent relationships across sessions

###  CLI Experience

* Clean terminal UI using `rich`
* Structured tables and colored output
* Human-readable task urgency system

### Testing

* Automated tests using `pytest`
* Relationship validation (User → Project → Task flow)
* CRUD lifecycle testing

---

##  Project Architecture

```
project-management-cli/
│
├── main.py
│
├── cli/
│   ├── parser.py          # argparse CLI structure
│   └── commands.py        # command routing layer
│
├── models/
│   ├── base_model.py      # shared ID + timestamps
│   ├── user.py
│   ├── project.py
│   └── task.py
│
├── schemas/
│   ├── user_schema.py
│   ├── project_schema.py
│   └── task_schema.py
│
├── services/
│   ├── user_service.py
│   ├── project_service.py
│   ├── task_service.py
│   └── dashboard_service.py
│
├── storage/
│   └── json_db.py         # file I/O abstraction layer
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

## stallation

### 1. Clone Repository

```bash
git clone 
cd project-management-cli
```

---

### 2. Install Dependencies (Pipenv)

```bash
pip install pipenv
pipenv install
pipenv shell
```

---

### 3. Install Required Extras

```bash
pipenv install rich
pipenv install "pydantic[email]"
```

---

## ▶Running the Application

```bash
python main.py <command> [options]
```

---

### Example

```bash
python main.py user add --name "Alex" --email "alex@mail.com"
```

---

##  CLI Commands

---

### User Commands

```bash
user add --name "Alex" --email "alex@mail.com"
user list
```

---

###  Project Commands

```bash
project add --user "Alex" --title "CLI Tool"
project list --user "Alex"
project search --keyword "CLI"
```

---

###  Task Commands

```bash
task add --project "CLI Tool" --title "Build CLI parser" --due 2026-06-15
task list --project "CLI Tool"
task list --overdue
task list --due-soon
task list --assigned "Alex"
task complete --title "Build CLI parser"
task search --keyword "parser"
```

---

### Dashboard

```bash
dashboard
```

---

## Data Persistence

All data is stored locally in JSON format:

```
data/users.json
data/projects.json
data/tasks.json
```

The system uses a centralized storage layer (`json_db.py`) to ensure:

* consistent file access
* safe read/write operations
* structured persistence across all entities

---

##  Running Tests

```bash
pytest
```

### Test Coverage Includes:

* User CRUD lifecycle
* Project-user relationships
* Task lifecycle (create → complete)
* Cross-entity validation
* Data persistence integrity
* CLI workflow validation

---

##  System Design

###  Architecture Style

The project follows a **layered architecture pattern**:

* CLI Layer → input handling (argparse)
* Service Layer → business logic
* Model Layer → data structure + behavior
* Storage Layer → persistence (JSON)
* Schema Layer → validation (Pydantic)

---

###  Relationships

* User → Projects (1-to-many)
* Project → Tasks (1-to-many)
* User →  Tasks (via project assignment)

---

##  Technologies Used

* Python 3.14
* argparse (CLI framework)
* JSON (data storage)
* rich (terminal UI formatting)
* pytest (unit testing)
* pydantic (validation)
* pipenv (dependency management)

---

## Key Design Highlights

* Clean separation of concerns
* Reusable service-layer architecture
* Real-world entity relationships
* Smart task urgency system
* Filterable CLI experience
* Extensible CRUD design

---

##  Author

Developed as part of a **Python OOP + CLI Systems Engineering Project**, demonstrating:

* real-world backend architecture design
* modular Python development
* CLI application engineering
* test-driven development practices

---

## License

This project is intended for **educational and academic use only**.

---