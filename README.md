# ReciPi
ReciPi developed for RaspberryPi 3B+, Ubuntu-Server 20.04.5 (64-bit)

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
## Virtualenv
- . venv/bin/activate
## The following are needed for opencv
- sudo apt-get update && sudo apt-get upgrade 
- sudo apt install -y build-essential cmake pkg-config libjpeg-dev libtiff5-dev libpng-dev libavcodec-dev libavformat-dev libswscale-dev libv4l-dev libxvidcore-dev libx264-dev libfontconfig1-dev libcairo2-dev libgdk-pixbuf2.0-dev libpango1.0-dev libgtk2.0-dev libgtk-3-dev libatlas-base-dev gfortran libhdf5-dev libhdf5-serial-dev libhdf5-103 libqt5gui5 libqt5webkit5 libqt5test5 python3-pyqt5 python3-dev
- pip install -r requirements.txt
## MongoDB
```
# Install the MongoDB 4.4 GPG key:
wget -qO - https://www.mongodb.org/static/pgp/server-4.4.asc | sudo apt-key add -

# Add the source location for the MongoDB packages:
echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu focal/mongodb-org/4.4 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-4.4.list

# Download the package details for the MongoDB packages:
sudo apt-get update

# Install MongoDB:
sudo apt-get install -y mongodb-org

# Ensure mongod config is picked up:
sudo systemctl daemon-reload

# Tell systemd to run mongod on reboot:
sudo systemctl enable mongod

# Start up mongod!
sudo systemctl start mongod

#Should return "Active: active"
sudo systemctl status mongod
```