# 💼 Django Expense Manager API

This is the backend for the **Expense Manager App** built using **Django** and **Django REST Framework (DRF)**. It supports full **JWT authentication & authorization**, and provides secure **CRUD API endpoints** for managing user-specific expenses.

---

## ✨ Features

- ✅ User Registration & Login
- 🔐 JWT-based Authentication & Authorization
- ➕ Create Expense
- 📝 Update Expense
- ❌ Delete Expense
- 📥 Get Expenses (user-specific)
- 🔄 RESTful API endpoints
- ⚙️ Admin panel for superuser management

---

## 🛠 Tech Stack

- **Python 3.x**
- **Django 5.x**
- **Django REST Framework**
- **Simple JWT** for authentication
- **PostgreSQL
- **CORS** support for frontend integration (e.g., React Native)

---

## 📦 Installation

```bash
git clone https://github.com/your-username/django-expense-api.git
cd django-expense-api
python -m venv env
source env/bin/activate  # for Linux/macOS
env\Scripts\activate     # for Windows
pip install -r requirements.txt

## Setup and Installation

### Prerequisites

- Python 3.x installed
- pip (Python package installer)
- Virtual environment tool (optional but recommended)

### Steps

1. **Clone the Repository**

   git clone https://github.com/yourusername/django-expense-app-backend.git
   cd django-expense-app-backend
2.Add a setting.py
3.pip install -r requirements.txt
   ```

## Apply Migrations
- python manage.py makemigrations
- python manage.py migrate

## Run server locally
- python manage.py runserver



