import sqlite3
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        if username == "admin" and password == "admin123":
            return redirect("/dashboard")

        return "Invalid Login"

    return render_template("login.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/add-crop", methods=["GET", "POST"])
def add_crop():

    if request.method == "POST":

        crop_name = request.form["crop_name"]
        location = request.form["location"]
        yield_amount = request.form["yield_amount"]

        conn = sqlite3.connect("harvestiq.db")
        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO crops
        (crop_name, location, yield_amount)
        VALUES (?, ?, ?)
        """, (crop_name, location, yield_amount))

        conn.commit()
        conn.close()

        return "Crop Saved Successfully!"

    return render_template("add_crop.html")

if __name__ == "__main__":
    app.run(debug=True)