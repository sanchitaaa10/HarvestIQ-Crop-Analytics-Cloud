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

    conn = sqlite3.connect("harvestiq.db")
    cursor = conn.cursor()

    # Total Crops
    cursor.execute("SELECT COUNT(*) FROM crops")
    total_crops = cursor.fetchone()[0]

    # Total Yield
    cursor.execute("SELECT SUM(yield_amount) FROM crops")
    total_yield = cursor.fetchone()[0]

    if total_yield is None:
        total_yield = 0

    # Total Locations
    cursor.execute("SELECT COUNT(DISTINCT location) FROM crops")
    total_locations = cursor.fetchone()[0]

    conn.close()

    return render_template(
        "dashboard.html",
        total_crops=total_crops,
        total_yield=total_yield,
        total_locations=total_locations
    )

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

@app.route("/test")
def test():

    conn = sqlite3.connect("harvestiq.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM crops")

    data = cursor.fetchall()

    conn.close()

    return str(data)


@app.route("/crops")
def view_crops():

    conn = sqlite3.connect("harvestiq.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM crops")
    crops = cursor.fetchall()

    conn.close()

    return render_template(
        "crops.html",
        crops=crops
    )
@app.route("/delete/<int:id>")
def delete_crop(id):

    conn = sqlite3.connect("harvestiq.db")
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM crops WHERE id=?",
        (id,)
    )

    conn.commit()
    conn.close()

    return redirect("/crops")

@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit_crop(id):

    conn = sqlite3.connect("harvestiq.db")
    cursor = conn.cursor()

    if request.method == "POST":

        crop_name = request.form["crop_name"]
        location = request.form["location"]
        yield_amount = request.form["yield_amount"]

        cursor.execute("""
        UPDATE crops
        SET crop_name=?,
            location=?,
            yield_amount=?
        WHERE id=?
        """, (
            crop_name,
            location,
            yield_amount,
            id
        ))

        conn.commit()
        conn.close()

        return redirect("/crops")

    cursor.execute(
        "SELECT * FROM crops WHERE id=?",
        (id,)
    )

    crop = cursor.fetchone()

    conn.close()

    return render_template(
        "edit_crop.html",
        crop=crop
    )

@app.route("/reports")
def reports():

    conn = sqlite3.connect("harvestiq.db")
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM crops")
    total_crops = cursor.fetchone()[0]

    cursor.execute("SELECT SUM(yield_amount) FROM crops")
    total_yield = cursor.fetchone()[0]

    if total_yield is None:
        total_yield = 0

    cursor.execute("SELECT COUNT(DISTINCT location) FROM crops")
    total_locations = cursor.fetchone()[0]

    conn.close()

    return render_template(
        "reports.html",
        total_crops=total_crops,
        total_yield=total_yield,
        total_locations=total_locations
    )



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)