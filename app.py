from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!!</p>"


@app.route("/<name>")
def hello(name):
    return f"Hello, {name}!"


app.run(host='0.0.0.0', port=8080)

