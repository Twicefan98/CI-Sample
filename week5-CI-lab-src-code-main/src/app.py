import flask
import time

app = flask.Flask(__name__)


@app.route("/")
def index():
    return "Welcome!!! ", time.localtime
# New Line to end the file