from flask import Flask
from flask.json import jsonify


app = Flask(__name__)  # define main file Flask("main.py")


dict_primjer = {
    "Ime": "Marko",
    "Prezime": "Markic",
    "Email": "marko@mail.com",
}


# set default route
@app.route("/")
def home():
    return "<h1><a href='/about'>Hello World</a></h1>"


@app.route("/about")
def about_page():
    return "<p>About page</p>"


# links such as localhost/user/Marko will work
@app.route("/user/<username>")
def user(username):
    return f"<h3>User page for {username}</hr>"


# If you want get json 'dict_primjer' just execute route localhost/json
@app.route("/json")
def json():
    return jsonify(dict_primjer)


@app.route("/json/<key>")
def json_value(key):
    return dict_primjer.get(key, "Unknovn key")


# moramo zamjenit retke sa tupcima, prazne podatke
# te drugi redak u kojem pise doubles