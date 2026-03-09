📝 Django Simple Blog

A simple Blog Web Application built with Django that allows users to create, view, update, delete, and search posts.

This project was built to practice Django CRUD operations, search functionality, and working with categories.

🚀 Features

Create new blog posts

View all posts in a table

Update existing posts

Delete posts

Search posts by title

Filter posts by category

Display post creation date

Simple and clean interface

🖥️ Project Preview
All Posts Page

🛠️ Built With

Python

Django

HTML


SQLite

📂 Project Structure
blog_project/
│
├── blog_app/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│
├── templates/
│    ├── pages
│    │   ├── all_p.html
│    │   ├── add_p.html
│    │   ├── add_cat.html
│    │   ├── edit_p.html
│    │   ├── delete_p.html
│    ├──main.html 
├── db.sqlite3
├── manage.py
⚙️ Installation

1️⃣ Clone the repository

git clone https://github.com/Firas-coder/Django-Mini-Blog

2️⃣ Go to mini_blog_sys_proj

cd project_name

3️⃣ Create virtual environment

python -m venv pyvenv

4️⃣ Activate virtual environment

Windows:

pyvenv\Scripts\activate

5️⃣ Install dependencies

pip install django

6️⃣ Run migrations

python manage.py migrate

7️⃣ Run the server

login admin site
  user name : admin
  password : 1234

python manage.py runserver

Open in browser:

http://127.0.0.1:8000/
📚 What I Learned

Django Models

Django Forms

CRUD Operations

Search & Filtering

Django Templates

Handling Query Parameters

👨‍💻 Author

ZeroPyteCode

Junior Backend Developer | Django & Python
Building real-world Django projects to improve backend skills.

GitHub:
https://github.com/Firas-coder
