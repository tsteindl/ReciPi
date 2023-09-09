import numpy as np
import cv2
import sqlite3
from pyzbar import pyzbar
from time import sleep


def draw_barcode(decoded, image):
    # n_points = len(decoded.polygon)
    # for i in range(n_points):
    #     image = cv2.line(image, decoded.polygon[i], decoded.polygon[(i+1) % n_points], color=(0, 255, 0), thickness=5)
    # uncomment above and comment below if you want to draw a polygon and not a rectangle
    image = cv2.rectangle(image, (decoded.rect.left, decoded.rect.top), 
                            (decoded.rect.left + decoded.rect.width, decoded.rect.top + decoded.rect.height),
                            color=(0, 255, 0),
                            thickness=5)
    return image

def decode(image):
    """
    returns image, objects
    """
    # decodes all barcodes from an image
    decoded_objects = pyzbar.decode(image, symbols=[pyzbar.ZBarSymbol.QRCODE, pyzbar.ZBarSymbol.EAN13])
    for obj in decoded_objects:
        # draw the barcode
        print("detected barcode:", obj)
        # image = draw_barcode(obj, image)
        # print barcode type & data
        print("Type:", obj.type)
        print("Data:", obj.data)
        print()

    return image, decoded_objects


connection = sqlite3.connect('/home/pi/Projects/ReciPi/db/recipi.db')
cursor = connection.cursor()

# Create the "barcodes" table with schema
cursor.execute('''
    CREATE TABLE IF NOT EXISTS barcodes (
        id INTEGER PRIMARY KEY,
        timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        barcode_type TEXT,
        barcode_data BLOB NOT NULL,
        quality INTEGER,
        orientation TEXT,
        UNIQUE (barcode_data) -- Ensure barcode data is unique
    )
''')



cap = cv2.VideoCapture(-1)

while(True):
    # Capture frame-by-frame
    # sleep(1)
    ret, frame = cap.read()

    # if not ret:
        # continue
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    frame, barcodes = decode(gray)

    for barcode in barcodes:
        #database insert
        cursor.execute('''
            INSERT OR IGNORE INTO barcodes
            (barcode_type, barcode_data, quality, orientation)
            VALUES (?, ?, ?, ?)
        ''', (
            barcode.type,
            barcode.data,
            barcode.quality,
            barcode.orientation
        ))
        # print("Inserted: " + connection.insert_id())

    # Display the resulting frame
    # cv2.imshow('frame', gray)
    cv2.imshow('frame', frame)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
connection.commit()
cap.release()
cv2.destroyAllWindows()




