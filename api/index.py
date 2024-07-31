from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def file():
    return render_template("aframe.html")

if __name__ == "__main__":
    app.run(port=8000,debug=True)   