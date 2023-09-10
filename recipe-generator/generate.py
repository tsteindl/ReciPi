import sqlite3
import json

import sys
sys.path.insert(1, sys.path[0] + "/../")
from config import DB_PATH, OPEN_EAN_USER_ID


connection = sqlite3.connect(DB_PATH)
cursor = connection.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS recipes (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        description TEXT NOT NULL,
        prompt TEXT,
        url TEXT,
        timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
''')
               
cursor.execute('''
    CREATE TABLE IF NOT EXISTS recipes_products (
        recipe_id INTEGER,
        product_id INTEGER,
        FOREIGN KEY (recipe_id) REFERENCES recipe(id),
        FOREIGN KEY (product_id) REFERENCES product(id)
    )
''')


#generate prompt
cursor.execute("SELECT id, name, detailname FROM products")
products = cursor.fetchall()

cursor.execute("SELECT id, name FROM recipes")
recipes = cursor.fetchall()

if len(products) == 0:
    print("You have no ingredients available. Exiting...")
    exit()

prompt = "Please suggest me a recipe with the following ingredients (id, name), you do not have to use all ingredients.\n"
prompt += ", ".join([f"({id},{name})" for id, name, detailname in products]) + ".\n\n"
prompt += "These are the recipes I have already cooked:\n"
prompt += ", ".join([name for id, name in recipes]) + ".\n\n"
prompt += "Generate your answer in German and in the following format.\n{'name': name of dish, 'ingredients': [[id of first ingredient, name of first ingredient], [id of second ingredient, name of second ingredient], ...]}, 'recipe': the instructions.\n"
prompt += "If you used an ingredient that I did not tell you, use the format (-1, name of the ingredient)"

#api call with prompt
print(prompt)
print()
response_text = input("Recipe: ")
response_json = json.loads(response_text)

print(response_json["recipe"])

#persist recipe in database
cursor.execute("""
    INSERT INTO recipes (name, description, prompt, url)
    VALUES (?, ?, ?, ?)
    """, (
        response_json["name"],
        response_json["recipe"],
        prompt,
        "www.google.com" #TODO change
        )
    )

recipe_id = cursor.lastrowid
ids_arr = []
for product in response_json["ingredients"]:
    product_id = product[0]
    if product_id != -1:
        ids_arr.append((recipe_id, product_id))

#Bulk insert
cursor.executemany("""
    INSERT INTO recipes_products (recipe_id, product_id)
    VALUES (?, ?)
    """, (
    ((ids[0], ids[1]) for ids in ids_arr)
))

#TODO remove consumed products from table

# Commit changes
connection.commit()

# Close the connection
connection.close()