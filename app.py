from flask import Flask


app = Flask(__name__)
req_count = 1


@app.route("/")
def hello_world():
    return "<p>Hello, World!!</p>"


@app.route("/healthz")
def health_check():
    global req_count

    req_count += 1
    if req_count > 40:
        return "", 500
    else:
        return "", 200


@app.route("/<name>")
def hello(name):
    return f"Hello, {name}!"


app.run(host='0.0.0.0', port=8080)

