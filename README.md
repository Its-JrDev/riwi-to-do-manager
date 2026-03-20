# 🧑‍💻 To-Do Manager (Console App)

## 📌 Description

A console-based task management application built with Python.
It allows users to create, view, update, and delete tasks, with input validation and filtering by status.

---

## 🧩 Features

* Create tasks (title, description, priority, status)
* View all tasks
* Filter tasks by:

  * Pending
  * Completed
* Update task status
* Delete tasks with confirmation
* Input validation for all user entries

---

## 📂 Project Structure

```
riwi-to-do-manager/
├─ src/
│  ├─ main.py
│  ├─ menu.py
│  ├─ validations.py
│  ├─ services.py
│  └─ models.py
├─ README.md
├─ .gitignore
└─ requirements.txt
```

---

## ▶️ How to Run

```bash
python src/main.py
```

---

## 🧪 Validations

The system ensures:

* Numeric inputs are valid and within range
* Strings are not empty
* Priority must be: `high`, `medium`, `low`
* Status must be: `pending`, `completed`

---

## ⚙️ Technical Notes

* Tasks are stored in memory (no persistence yet)
* Data is lost when the program exits
* No external libraries are required

---

## 🧠 Learning Focus

### Python

* Functions and modularization
* CRUD operations
* Input validation
* Control flow (`if`, `while`, `for`)

### Git Workflow

* Feature branches
* Pull Requests
* Merge into `develop`

---

## 🚧 Pending Improvements

* Add persistent storage (JSON or database)
* Implement task IDs instead of title-based search
* Improve error handling (optional try/except)
* Add more documentation
* Create release tag `v1.0.0`

---

## 👥 Collaborators

* @Its-JrDev
* @AndrxsGutierrez
* @emmanuelarchi30-alt
* @Jgonzalez-2005
* @jhonata0200p
* @JoshuaQ-rJ
