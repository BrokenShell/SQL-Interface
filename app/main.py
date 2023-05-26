from app.database import DatabaseInterface


db = DatabaseInterface()
query = "SELECT * FROM charactercreator_character"
result = db.fetch_data(query)

for row in result:
    print(row)

db.disconnect()
