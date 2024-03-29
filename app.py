from flask import Flask, render_template
import pandas as pd
import requests
app = Flask(__name__)
data = pd.read_json(r'./static/chat.json',orient='records')
data = data.to_dict()

@app.route('/')
def index():
    return render_template('space.html')

@app.route("/about")
def about():
    return render_template("index.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/video",methods=['GET','POST'])
def video():
    # requests.get(url='http://127.0.0.1:5000/static/script.js')
    return render_template("try.html")
if __name__ == '__main__':
    app.run(debug=True)
