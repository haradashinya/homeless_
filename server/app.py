#coding: utf-8


from flask import Flask,render_template
from models.user import User

app = Flask(__name__)

@app.route("/")
def hello():
    return "hello"

# register user
@app.route("/users/<username>",methods=["POST"])
def create():
    user = User("nobi")

    return "hello"


if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5001,debug=True)


