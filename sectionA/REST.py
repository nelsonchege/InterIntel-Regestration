from flask import Flask, request


app = Flask(__name__)


@app.route("/")
def index():
    return "hello world"


@app.route("/methods", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        return "message from post message"
    if request.method == "GET":
        return "message from get message"


if __name__ == "__main__":
    app.run(debug=True)
