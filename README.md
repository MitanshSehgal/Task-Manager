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
1. **Simple Hello World app**
2. **Setup database connection** & sign up for MongoDB Cloud
3. **Setup `run.py` file** (Project Configurations)
4. **Setup Base Template**
5. **Setup `view.html` file**
6. **Create Flask Forms**
7. **Implement Insert Operation**
8. **Implement Sweet Alerts**
9. **Implement Retrieve Operation**
10. **Implement Delete Operation**
11. **Implement Update Functionality**
12. **Setup `.gitignore` file**

---
This guide will help you build a full CRUD application with Flask and MongoDB. 🚀
