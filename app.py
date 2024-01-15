from flask import Flask,Request,Response,render_template
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "yoo"

if __name__ == "__main__":
    app.run(debug=True)