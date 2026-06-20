import boto3
import pymysql
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# =========================
# S3 Configuration
# =========================

s3 = boto3.client('s3')
BUCKET_NAME = "harvestiq-sanchita-2026"

# =========================
# MySQL Connection
# =========================

def get_connection():
    return pymysql.connect(
        host="harvestiq-db.cduao8yi8dwl.ap-south-1.rds.amazonaws.com",
        user="admin",
        password="Admin123",
        database="harvestiq"
    )

# =========================
# File Upload to S3
# =========================

@app.route("/upload", methods=["GET", "POST"])
def upload_file():

    if request.method == "POST":

        file = request.files["file"]

        s3.upload_fileobj(
            file,
            BUCKET_NAME,
            file.filename
        )

        return "Uploaded Successfully!"

    return """
    <form method="POST" enctype="multipart/form-data">
        <input type="file" name="file">
        <button type="submit">Upload</button>
    </form>
    """

# =========================
# Login
# =========================

@app.route("/", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        if username == "admin" and password == "admin123":
            return redirect("/dashboard")

        return "Invalid Login"

    return render_template("login.html")

# =========================
# Dashboard
# =========================

@app.route("/dashboard")
def dashboard():

    conn = get_connection()
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
        "dashboard.html",
        total_crops=total_crops,
        total_yield=total_yield,
        total_locations=total_locations
    )

# =========================
# Add Crop
# =========================

@app.route("/add-crop", methods=["GET", "POST"])
def add_crop():

    if request.method == "POST":

        crop_name = request.form["crop_name"]
        location = request.form["location"]
        yield_amount = request.form["yield_amount"]

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO crops
            (crop_name, location, yield_amount)
            VALUES (%s, %s, %s)
        """, (crop_name, location, yield_amount))

        conn.commit()
        conn.close()

        return "Crop Saved Successfully!"

    return render_template("add_crop.html")

# =========================
# View Crops
# =========================

@app.route("/crops")
def view_crops():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM crops")
    crops = cursor.fetchall()

    conn.close()

    return render_template(
        "crops.html",
        crops=crops
    )

# =========================
# Delete Crop
# =========================

@app.route("/delete/<int:id>")
def delete_crop(id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM crops WHERE id=%s",
        (id,)
    )

    conn.commit()
    conn.close()

    return redirect("/crops")

# =========================
# Edit Crop
# =========================

@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit_crop(id):

    conn = get_connection()
    cursor = conn.cursor()

    if request.method == "POST":

        crop_name = request.form["crop_name"]
        location = request.form["location"]
        yield_amount = request.form["yield_amount"]

        cursor.execute("""
            UPDATE crops
            SET crop_name=%s,
                location=%s,
                yield_amount=%s
            WHERE id=%s
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
        "SELECT * FROM crops WHERE id=%s",
        (id,)
    )

    crop = cursor.fetchone()

    conn.close()

    return render_template(
        "edit_crop.html",
        crop=crop
    )

# =========================
# Reports
# =========================

@app.route("/reports")
def reports():

    conn = get_connection()
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

# =========================
# Test Route
# =========================

@app.route("/test")
def test():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM crops")
    data = cursor.fetchall()

    conn.close()

    return str(data)

# =========================
# Main
# =========================

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)