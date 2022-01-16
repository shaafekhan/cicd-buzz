import os
from flask import Flask

app = Flask(__name__)


@app.route("/")
def generate_buzz():
    page = '<html><body><h1>'
    page += "Greetings from Shaafe </br>"
    page += '</h1></body></html>'
    return page


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 5000)))
