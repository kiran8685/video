from flask import Flask, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy
import pandas as pd
import sqlite3
import smtplib
import requests
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///LMT.db"
# app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////LMT.db"
db = SQLAlchemy(app)
data = pd.read_json(r'./static/chat.json',orient='records')
data = data.to_dict()

class Query(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(10), nullable = False)
    last_name = db.Column(db.String(10), nullable = False)
    email = db.Column(db.String(20), nullable = True)
    message = db.Column(db.String(500), nullable = False)
    
    def __repr__(self) -> str:
        return f"{self.first_name} we will get back to you soon!"

@app.route('/')
def index():
    return render_template('space.html')

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact",methods=['GET','POST'])
def contact():
    try:
        if request.method == "POST":
            first_name = request.form['first_name']
            last_name = request.form['last_name']
            email = request.form["email"]
            message = request.form["message"]
            query = Query(first_name=first_name,last_name=last_name,email=email,message=message)
            db.session.add(query)
            db.session.commit()
    except sqlite3.IntegrityError:
        return redirect("/contact.html")
    except  Exception as e:
        print(e)
        return redirect("/contact.html")
        
        
    return render_template("contact.html")

if __name__ == '__main__':
    
    app.run(debug=True)
