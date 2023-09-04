# ReciPi
ReciPi developed for RaspberryPi 3B+

## Sources:
- [How to Install OpenCV on a Raspberry Pi](https://www.youtube.com/watch?v=QzVYnG-WaM4)
- https://en.wikipedia.org/wiki/Barcode
- https://thepythoncode.com/article/making-a-barcode-scanner-in-python
- [Install MongoDB](https://www.mongodb.com/developer/products/mongodb/mongodb-on-raspberry-pi/)
- https://hub.docker.com/r/andresvidal/rpi3-mongodb3/

# TODOs
## Barcode Scanner
- install sense hat
- install opencv
- capture image
- search for product with api call
- setup database
- upload to database
- make script for setting up database

## Data Model
- checkmark on sensehat

## Recipe Creater
- generate ChatGPT Query
- setup chatgpt API
- Find way to interact with program 

# How to use
- . venv/bin/activate
- sudo apt-get update && sudo apt-get upgrade 
 - sudo apt install -y build-essential cmake pkg-config libjpeg-dev libtiff5-dev libpng-dev libavcodec-dev libavformat-dev libswscale-dev libv4l-dev libxvidcore-dev libx264-dev libfontconfig1-dev libcairo2-dev libgdk-pixbuf2.0-dev libpango1.0-dev libgtk2.0-dev libgtk-3-dev libatlas-base-dev gfortran libhdf5-dev libhdf5-serial-dev libhdf5-103 libqt5gui5 libqt5webkit5 libqt5test5 python3-pyqt5 python3-dev
- pip install -r requirements.txt
- Run MongoDB database
- python main.p