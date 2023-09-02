#Python base image from https://hub.docker.com/r/arm32v7/python/
FROM arm32v7/python:3.11.5-bullseye

#like 'cd' command
WORKDIR /app 

RUN apt-get update && apt install -y
    # sense-hat \
    # python-smbus \
    # i2c-tools

COPY requirements.txt ./

RUN pip install --no-cache-dir --upgrade pip \
  && pip install --no-cache-dir -r requirements.txt

#RUN pip install --no-cache-dir rpi.gpio


# RUN apt-get update && apt-get install -y \
#     package-bar \
#     package-baz \
#     package-foo  \
#     && rm -rf /var/lib/apt/lists/*

COPY . .

#ENV PORT=8080

#EXPOSE 8080

# Trigger Python script
CMD ["python", "./barcode-scanner/sense_hat.py"]