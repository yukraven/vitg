import sqlite3
import Sources.Parser

conn = sqlite3.connect("Database/vitg.db")

cursor = conn.cursor()
cursor.execute("SELECT * FROM Locations")
results = cursor.fetchall()
print(results)

conn.close()

parser = Sources.Parser.Parser()
words = [u"любить", u"бить"]
for word in words:
    command = parser.getCommand(word)
    print(command)
