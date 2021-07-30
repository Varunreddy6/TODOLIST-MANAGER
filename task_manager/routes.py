from task_manager import app
from flask import render_template, url_for, redirect, request
from task_manager.models import Todo
from task_manager import db
import time
from datetime import datetime,date

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        task_content = request.form['content']
        task_deadline =request.form.get('deadline')
        task_deadline =datetime.strptime(task_deadline,'%Y-%m-%d')
        new_task = Todo(content=task_content,deadline=task_deadline)
        
        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')

        except:
            return (task_deadline+"1")

    else:
        tasks = Todo.query.order_by(Todo.time_stamp).all()
        for task in tasks:
            if date.today()>task.deadline and task.status!="finished":
                task.status="overdue"

        
        return render_template('index.html', tasks=tasks)



@app.route("/finish/<int:id>")
def finish(id):
    task_to_delete = Todo.query.get_or_404(id)
    #task_to_delete.time_stamp=datetime.datetime.utcnow()
    task_to_delete.time_stamp= (datetime.utcnow()-task_to_delete.time_stamp)
    task_to_delete.days=int(task_to_delete.time_stamp.days)
    task_to_delete.hours=int(task_to_delete.time_stamp.total_seconds()/3600)
    task_to_delete.minutes=int(task_to_delete.time_stamp.total_seconds()/60)
    task_to_delete.seconds=int(task_to_delete.time_stamp.total_seconds())

    return render_template('finish.html' , task=task_to_delete)

@app.route("/Yes/<int:id>")
def Yes(id , methods=['POST']):
    task_to_delete = Todo.query.get_or_404(id)
    if request.method == "GET":
        task_to_delete.status ="finished"

        try:
            db.session.commit()
            return redirect('/')
        except:
            return "there was some issue processing"
    return "issue with if loop"
    
    

@app.route("/update/<int:id>", methods=['GET', 'POST'])
def update(id):
    task_to_update = Todo.query.get_or_404(id)

    if request.method == "POST":
        task_to_update.content = request.form['content']

        try:
            db.session.commit()
            return redirect('/')

        except:
            return "There was an issue updating your task!"

    else:
        return render_template('update.html', task=task_to_update)

@app.route("/delete/<int:id>")
def delete(id):
    task_to_delete = Todo.query.get_or_404(id)
    try:
       # time_
            db.session.delete(task_to_delete)
            db.session.commit()
            return redirect('/')

    except:
        return "There was an issue deleting that task!"







