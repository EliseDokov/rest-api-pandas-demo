from flask import Flask


app = Flask(__name__)  # define main file Flask("main.py")

# set default route
@app.route("/")
def hello_world():
    return "<p>Hello World</p>"

@app.route("/about")
def about_page():
    return "<p>About page</p>"