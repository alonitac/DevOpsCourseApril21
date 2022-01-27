from flask import Flask
req_red = 1
app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/<name>")
def hello(name):
    return f"Hello, {name}!"



@app.route("/healthz")
def healthcheck():
    global req_red
    req_red += 1
    if req_red > 20:
        return "" , 200
    return "" , 500




app.run(host='0.0.0.0', port=8080)

