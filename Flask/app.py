from flask import Flask

### WSGI Application

app = Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome to this Flask app"

@app.route("/index")
def index():
    return "Welcome to the Index page"

if __name__ == "__main__":
    app.run(debug=True)