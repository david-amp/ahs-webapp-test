import Flask as Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return 'Hello World!\n'
