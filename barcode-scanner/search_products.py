import sqlite3
import sys
import requests
import json

sys.path.insert(1, sys.path[0] + "/../")
from config import DB_PATH, OPEN_EAN_USER_ID

connection = sqlite3.connect(DB_PATH)
cursor = connection.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        detailname TEXT,
        vendor TEXT,
        maincat TEXT,
        subcat TEXT,
        contents INTEGER,
        pack INTEGER,
        descr TEXT,
        origin TEXT,
        validated INTEGER,
        url TEXT,
        barcode_id INTEGER,
        downloaded_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (barcode_id) REFERENCES barcodes(id)
    )
''')


# Select all barcodes from the "barcodes" table
cursor.execute("SELECT id, barcode_data FROM barcodes")

# Fetch all the rows as a list of tuples
barcodes = cursor.fetchall()

for barcode_id, barcode_data in barcodes:
    print(f"Fetching data for barcode: {barcode_data}...")
    # http://opengtindb.org/?ean=[ean]&cmd=query&queryid=[userid]
    url = f"http://opengtindb.org/?ean={barcode_data}&cmd=query&queryid={OPEN_EAN_USER_ID}"

    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # The API response content can be accessed using response.text
        reponse_text = response.text.encode("utf-8").decode("utf-8)")
        print(response.text)
        if 'error=1' in reponse_text:
            continue
        elif 'error=0' in reponse_text:
            """
            error=0
            ---
            name=Natürliches Mineralwasser
            detailname=Bad Vilbeler RIED Quelle
            vendor=H. Kroner GmbH & CO. KG
            maincat=Getränke, Alkohol
            subcat=
            contents=19
            pack=1
            descr=Natürliches Mineralwasser mit Kohlensäure versetzt
            origin=Deutschland
            validated=25 %
            ---
            """

            api_data = {item[0]: item[1] for item in [row.split("=") for row in reponse_text.split("\n") if row and row != "---"]}
            print("Found product: ")
            print(json.dumps(api_data, indent=4))
            cursor.execute("""
                INSERT OR IGNORE INTO products
                (name, detailname, vendor, maincat, subcat, contents, pack, descr, origin, validated, url, barcode_id)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                api_data["name"],
                api_data["detailname"],
                api_data["vendor"],
                api_data["maincat"],
                api_data["subcat"],
                api_data["contents"],
                api_data["pack"],
                api_data["descr"],
                api_data["origin"],
                api_data["validated"],
                url,
                barcode_id
            )
            )
    else:
        print(f"Request failed with status code: {response.status_code}")



# Commit changes
connection.commit()

# Close the connection
connection.close()