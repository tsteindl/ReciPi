# ReciPi
- ReciPi is a RaspberryPi project that is able to scan Barcodes using the camera module (or any USB camera) from grocery items, retrieve products from public database and store them into a SQLite database. Then user can prompt the program to query ChatGPT (or any other similar project) to generate a recipe. Recipes are also stored so they don't become redundant.
- Developed for RaspberryPi 3B+, Raspberry OS Lite (64-bit)


## Sources:
- [How to Install OpenCV on a Raspberry Pi](https://www.youtube.com/watch?v=QzVYnG-WaM4)
- https://en.wikipedia.org/wiki/Barcode
- https://thepythoncode.com/article/making-a-barcode-scanner-in-python
- [How to install SQLite](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-sqlite-on-ubuntu-20-04)
- [Enable Memory swaping](https://ubuntu.com/blog/how-low-can-you-go-running-ubuntu-desktop-on-a-2gb-raspberry-pi-4)
- [ChatGPT API Documentation](https://platform.openai.com/docs/guides/gpt)
- [Open EAN Database](https://opengtindb.org/)
- [EAN Search Database](https://www.ean-search.org/)
# TODOs
- datamodel with listener on barcode scans that automatically searches products
- puppeteer to access EAN-search and ChatGPT
- async requests
- remember already accessed barcodes
- improve camera resolution
- checkmark on sensehat

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
