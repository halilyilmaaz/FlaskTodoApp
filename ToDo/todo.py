from flask import Flask,render_template,request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////C:/Users/LENOVO/Desktop/ToDo/todo.db'
db = SQLAlchemy(app)


@app.route("/")
def index():
    todos = Todo.query.all()

    return render_template("index.html",todos=todos)
@app.route("/add",methods = ["POST"])
def addTodo():
    title = request.form.get("title")
    content = request.form.get("content")

    newTodo = Todo(title = title,content = content,complate = False) 
    db.session.add(newTodo)
    db.session.commit()
    return redirect(url_for("index"))

@app.route("/complate/<string:id>",methods=["GET"])
def complateTodo(id):
    todo = Todo.query.filter_by(id=id).first()

    if(todo.complate==False):
        todo.complate ==True
    else:
        todo.complate == False

    db.session.commit()

    return redirect(url_for("index"))

@app.route("/delete/<string:id>",methods=["GET"])
def deleteTodo(id):
    todo = Todo.query.filter_by(id=id).first()
    db.session.delete(todo)
    db.session.commit() 

    return redirect(url_for("index"))

class Todo(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(80))
    content = db.Column(db.Text)
    complate = db.Column(db.Boolean)

    



if __name__ == "__main__":
    app.run(debug = True)