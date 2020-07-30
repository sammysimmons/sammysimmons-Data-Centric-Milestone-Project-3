import os
import json
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/recipe")
def recipe():
    data = []
    with open("data/recipe.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("recipe.html", recipe=data)

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/register")
def register():
    return render_template("register.html")



if __name__ == '__main__':
           app.run(host=os.environ.get('IP', '127.0.0.1'),              
           port=int(os.environ.get('PORT', 5000)),
            debug=True)