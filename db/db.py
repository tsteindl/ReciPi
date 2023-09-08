import sqlite3

connection = sqlite3.connect('recipi.db')

cursor = connection.cursor()

# Create a table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS recipes (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        ingredients TEXT,
        instructions TEXT
    )
''')

cursor.execute("INSERT INTO recipes (name, ingredients, instructions) VALUES (?, ?, ?)",
               ("Chocolate Cake", "Flour, Sugar, Cocoa Powder", "1. Mix dry ingredients. 2. Add wet ingredients. 3. Bake at 350°F."))

# Commit changes
connection.commit()

# Query data
cursor.execute("SELECT * FROM recipes")
rows = cursor.fetchall()
for row in rows:
    print(row)

# Close the connection
connection.close()