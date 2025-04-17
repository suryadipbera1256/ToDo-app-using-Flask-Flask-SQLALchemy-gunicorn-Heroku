from turtle import title
from flask import Flask, redirect,render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy
import logging
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///ToDo.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db =SQLAlchemy(app)
class ToDo(db.Model):
    No =db.Column(db.Integer , primary_key = True)
    title = db.Column(db.String(200), nullable = False)
    desc = db.Column(db.String(500), nullable = False) 
    date_created = db.Column(db.DateTime , default = datetime.utcnow)

    def __repr__(self) -> str:
        return f"Todo({self.No},{self.title},{self.desc},{self.date_created})"


    @app.route('/' , methods =['GET','POST'])
    def hello_world():
        if request.method == 'POST':
            title = request.form['title']
            desc = request.form['desc']
            todo = ToDo(title = title, desc=desc)
            db.session.add(todo)
            db.session.commit()

        alltodo = ToDo.query.all()
        return render_template('index.html' , alltodo = alltodo)
    
    @app.route('/delete/<int:No>')
    def delete(No):
        todo = ToDo.query.filter_by(No = No).first()
        db.session.delete(todo)
        db.session.commit()
        return redirect('/')


    @app.route('/update/<int:No>', methods =['GET','POST'])
    def update(No):
        if request.method == 'POST':
            title = request.form['title']
            desc = request.form['desc']
            todo = ToDo.query.filter_by(No = No).first()
            todo.title = title
            todo.desc = desc
            db.session.add(todo)
            db.session.commit()
            return redirect('/')

        todo = ToDo.query.filter_by(No = No).first()
        return render_template('update.html', todo = todo)
    
        


if __name__ == "__main__":
    app.run(debug = True,port=8000)