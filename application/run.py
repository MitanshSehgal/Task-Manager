from flask import Flask, render_template, flash, request, redirect, url_for
from flask_pymongo import PyMongo
from forms import TodoForm
from werkzeug.utils import redirect
from datetime import datetime
from bson import ObjectId

app = Flask(__name__)

# App Configurations
app.config["SECRET_KEY"] = 'c9ae02f8730b71ad7bb70efa90203d87627fc32c'
app.config["MONGO_URI"] =  "mongodb+srv://mitanshs:mitanshsehgal@cluster0.7jableu.mongodb.net/mydatabase?retryWrites=true&w=majority&tls=true&tlsAllowInvalidCertificates=true"

# Setup MongoDB
mongodb_client = PyMongo(app)
db = mongodb_client.db
print(mongodb_client.db.list_collection_names())

@app.route('/')
def get_todos():
    try:
        todos = db.todos_flask.find().sort("date_created", -1)
        return render_template("view.html", title="Home", todos=todos)
    except Exception as e:
        flash("An error occurred", "danger")
        return redirect(url_for('get_todos'))

@app.route('/add_todos', methods=['POST', 'GET'])
def add_todos():
    form = TodoForm()
    if form.validate_on_submit():
        try:
            todo_name = form.name.data
            todo_description = form.description.data
            completed = form.completed.data

            db.todos_flask.insert_one({
                'name': todo_name,
                "description": todo_description,
                "completed": completed,
                "date_created": datetime.utcnow()
            })
            flash("Todo successfully added", "success")
        except Exception as e:
            flash("Database connection error!", "danger")
        return redirect(url_for('get_todos'))
    return render_template("addJob.html", form=form)

@app.route("/delete_todo/<id>")
def delete_todo(id):
    try:
        db.todos_flask.find_one_and_delete({"_id": ObjectId(id)})
        flash("Todo successfully deleted", "success")
    except Exception as e:
        flash("An error occurred", "danger")
    return redirect("/")

@app.route("/update_todo/<id>", methods = ['POST', 'GET'])
def update_todo(id):
    if request.method == "POST":
        form = TodoForm(request.form)
        todo_name = form.name.data
        todo_description = form.description.data
        completed = form.completed.data

        try:
            db.todos_flask.find_one_and_update({"_id": ObjectId(id)}, {"$set": {
                "name": todo_name,
                "description": todo_description,
                "completed": completed,
                "date_created": datetime.utcnow()
            }})
            flash("Todo successfully updated", "success")
        except Exception as e:
            flash("An error occurred", "danger")
        return redirect("/")
    else:
        form = TodoForm()

        try:
            todo = db.todos_flask.find_one_or_404({"_id": ObjectId(id)})
            form.name.data = todo.get("name", None)
            form.description.data = todo.get("description", None)
            form.completed.data = todo.get("completed", None)
        except Exception as e:
            flash("An error occurred", "danger")
        return render_template("addJob.html", form = form)

if __name__ == "__main__":
    app.run(debug=True)