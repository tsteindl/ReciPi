# ReciPi
ReciPi developed for RaspberryPi 3B+, Raspberry OS Lite (64-bit)

## Sources:
- [How to Install OpenCV on a Raspberry Pi](https://www.youtube.com/watch?v=QzVYnG-WaM4)
- https://en.wikipedia.org/wiki/Barcode
- https://thepythoncode.com/article/making-a-barcode-scanner-in-python
- [How to install SQLite](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-sqlite-on-ubuntu-20-04)
- [Enable Memory swaping](https://ubuntu.com/blog/how-low-can-you-go-running-ubuntu-desktop-on-a-2gb-raspberry-pi-4)
- [ChatGPT API Documentation](https://platform.openai.com/docs/guides/gpt)
# TODOs
## Barcode Scanner
- install sense hat
- install opencv
- capture image
- search for product with api call
- setup database
- upload to database
- make script for setting up database

- datamodel with listener on barcode scans that automatically searches products
- puppeteer to access EAN-search and ChatGPT
- async requests
- remember already accessed barcodes
- improve camera resolution so scanner works

## Data Model
- checkmark on sensehat

## Recipe Creater
- generate ChatGPT Query
- setup chatgpt API
- Find way to interact with program 

# How to use
## Virtualenv
- sudo pip install virtualenv
- virtualenv venv
- . venv/bin/activate
## The following are needed for opencv
```
sudo apt-get update && sudo apt-get upgrade 

sudo apt install -y build-essential cmake pkg-config libjpeg-dev libtiff5-dev libpng-dev libavcodec-dev libavformat-dev libswscale-dev libv4l-dev libxvidcore-dev libx264-dev libfontconfig1-dev libcairo2-dev libgdk-pixbuf2.0-dev libpango1.0-dev libgtk2.0-dev libgtk-3-dev libatlas-base-dev gfortran libhdf5-dev libhdf5-serial-dev libhdf5-103 libqt5gui5 libqt5webkit5 libqt5test5 python3-pyqt5 python3-dev

pip install -r requirements.txt

sudo apt-get install zbar-tools -y
```
## SQLite
```
sudo apt install sqlite3

sqlite3 recipi.db
```
- Change path to database in ???.py
- .open recipi.db
- PRAGMA table_info(table_name);