import sqlite3

conn = sqlite3.connect("Database/vitg.db")

cursor = conn.cursor()
cursor.execute("SELECT * FROM Locations")
results = cursor.fetchall()
print(results)

conn.close()