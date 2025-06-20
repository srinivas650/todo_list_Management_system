# Todo_List_Management_system
# 📝 Django To-Do List Management System

A full-stack web application built with Django that allows users to manage their daily tasks efficiently. Features include user authentication, task creation/editing/deletion, due dates, priorities, and completion tracking.

---

## 🚀 Features

- ✅ User registration and login (Django Auth)
- 🧾 Add, update, delete tasks
- ⏰ Set due dates and priority (High, Medium, Low)
- 📋 Mark tasks as complete/incomplete
- 📱 Responsive interface using Bootstrap
- 🔐 Data privacy — tasks are user-specific
- 🔍 Filter & view tasks by completion status

---

## 🛠️ Tech Stack

| Layer         | Technology           |
|---------------|----------------------|
| Backend       | Python, Django       |
| Frontend      | HTML, CSS, Bootstrap |
| Database      | SQLite               |
| Auth System   | Django Auth          |
| Dev Tools     | VS Code, Git, GitHub |

---

## 📸 Screenshots

> *(Add your own screenshots below by dragging .png/.jpg files into the repo)*

| Home Page | Task List |
|-----------|-----------|
| ![](screenshots/home.png) | ![](screenshots/tasks.png) |

---

## 🧑‍💻 Getting Started

### 🔧 Installation

```bash
git clone https://github.com/srinivas650/todo_list_Management_system.git
cd todo_list_Management_system
python -m venv venv
venv\Scripts\activate   # On Windows (use `source venv/bin/activate` on Linux/macOS)
pip install -r requirements.txt
python manage.py make migrations
python manage.py migrate
python manage.py runserver

---

Would you like this in a downloadable `.md` file or want me to auto-upload it to your GitHub repo through the next Git commit?
