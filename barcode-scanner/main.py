from time import sleep
from picamera import PiCamera
import cv2
from glob import glob
from scan import decode

camera = PiCamera() # Camera Access
camera.resolution = (1024, 768)
camera.start_preview()

camera.capture('image.jpg')
img = cv2.imread('image.jpg') # Load stored Image...
cv2.imshow('Recorded Image', img) #and display it


barcodes = glob("image*.jpg")
for barcode_file in barcodes:
    # load the image to opencv
    img = cv2.imread(barcode_file)
    # decode detected barcodes & get the image
    # that is drawn
    img = decode(img)
    # show the image
    cv2.imshow("img", img)
    cv2.waitKey(0)

cv2.waitKey(0)
cv2.destroyAllWindows()