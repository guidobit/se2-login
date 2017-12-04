from flask import Flask, jsonify, request, Response
app = Flask(__name__)


@app.route("/", methods=["GET"])
def hello():
    return "Hello World! Lets go, test!"


@app.route("/api/v1/login", methods=["POST"])
def login():
    return "login api"


@app.route("/api/v1/register", methods=["POST"])
def login():
    return "register api"


@app.route("/api/v1/logout", methods=["GET"])
def login():
    return "logout api"


@app.route("/api/v1/validate/token", methods=["POST"])
def login():
    return "validate/token api"


@app.route("/api/v1/publickey", methods=["GET"])
def login():
    return "publickey api"


if __name__ == "__main__":
    wildcard_interface = "0.0.0.0" # Runs on all available interfaces
    app.run(debug=True, host=wildcard_interface)


print('App started')