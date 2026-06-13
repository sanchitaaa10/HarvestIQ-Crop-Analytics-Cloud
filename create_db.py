import sqlite3

conn = sqlite3.connect("harvestiq.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS crops(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    crop_name TEXT,
    location TEXT,
    yield_amount REAL
)
""")

conn.commit()
conn.close()

print("Database Created Successfully")