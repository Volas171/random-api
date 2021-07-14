from flask import Flask,redirect
from flask import render_template

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/')
def home():
    return render_template('main.html')

app.run(host="0.0.0.0", port=8080)