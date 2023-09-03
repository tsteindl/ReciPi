# ReciPi
## Sources:
- [Learn Docker in 7 Easy Steps - Full Beginner's Tutorial](https://www.youtube.com/watch?v=gAkwW2tuIqE)
- https://iotbytes.wordpress.com/create-your-first-docker-container-for-raspberry-pi-to-blink-an-led/
- https://stackoverflow.com/questions/48957195/how-to-fix-docker-got-permission-denied-issue
- [Docker Local Development](https://vsupalov.com/rebuilding-docker-image-development/)
- [MongoDB in 100 Seconds](https://www.youtube.com/watch?v=-bt_y4Loofg)
- https://stackoverflow.com/questions/61365790/error-could-not-build-wheels-for-scipy-which-use-pep-517-and-cannot-be-installe
- https://stackoverflow.com/questions/63732353/error-could-not-build-wheels-for-opencv-python-which-use-pep-517-and-cannot-be/67855136#67855136

## Run
<!-- sudo docker build -t tsteindl/recipi:1-0 . -->
<!-- docker run --prvileged --name recipi -->
cd ReciPi
docker-compose up

# TODOs
## Barcode Scanner
- mount code without having to rebuild
- capture image
- search for product with api call
- setup database
- upload to database

## Data Model
- checkmark on sensehat

## Recipe Creater
- generate ChatGPT Query
- setup chatgpt API
- Find way to interact with program 
