# 📌 Flask MongoDB CRUD App
A CRUD (Create, Read, Update, Delete) application using Flask and MongoDB.

## 🚀 Project Setup
### 1️⃣ Create the Main Project Folder
Create a folder named **flaskMongoDB** (or your preferred name) for the project.

### 2️⃣ Create a Virtual Environment
#### Linux & Mac:
```bash
python -m venv venv
```
#### Windows:
```bash
python -m venv c:\path\to\myenv
```

### 3️⃣ Activate the Virtual Environment
#### Linux & Mac:
```bash
source venv/bin/activate
```
#### Windows:
```bash
venv\Scripts\activate.bat
```

### 4️⃣ Install Dependencies
```bash
pip install flask Flask-PyMongo Flask-WTF
python -m pip install "pymongo[srv]"
```

### 5️⃣ Setup MongoDB Cluster
Follow the official MongoDB documentation to set up your cloud database.

## 📂 Project Structure
```
project_root_dir
│
│__ application
|    │__ templates
|    │__ __init__.py
|    │__ routes.py
|    │__ forms.py
│
│__ venv
│
│__ README.md
│
│__ run.py
```

## 📝 Tutorial Phases
1️⃣ Simple **Hello World** app
2️⃣ Setup **database connection** & sign up for MongoDB Cloud
3️⃣ Setup `__init__.py` file (Project Configurations)
4️⃣ Setup **Base Template**
5️⃣ Setup `view_todos.html` file
6️⃣ Create **Flask Forms**
7️⃣ Implement **Insert Operation**
8️⃣ Implement **Sweet Alerts**
9️⃣ Implement **Retrieve Operation**
🔟 Implement **Delete Operation**
1️⃣1️⃣ Implement **Update Functionality**
1️⃣2️⃣ Setup **.gitignore** file

---
This guide will help you build a full CRUD application with Flask and MongoDB. 🚀
