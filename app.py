from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def login():
    return render_template("login.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/add-crop")
def add_crop():
    return render_template("add_crop.html")

if __name__ == "__main__":
    app.run(debug=True)

