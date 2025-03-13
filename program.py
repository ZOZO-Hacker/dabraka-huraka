from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>pocuvaj nejdě mi internet za čo ja ti platim ty geno!</p>"


@app.route("/huh")
def hevy():
    return "<h1>pocuvaj už mi dě internet za čo ja ti platim ty geno!</h1>"
