#!/usr/bin/python

import zbar
import Image
import time
import picamera
import RPi.GPIO as GPIO
import time

def getbarcode():
    with picamera.PiCamera() as camera:
        camera.resolution = (1024, 768)
        camera.start_preview()
        time.sleep(2) #�J����������
        camera.capture('barcode.jpg')

    # create a reader
    scanner = zbar.ImageScanner()

    # configure the reader
    scanner.parse_config('enable')

    # obtain image data
    pil = Image.open(barcode.jpg).convert('L')
    width, height = pil.size
    raw = pil.tostring()

    # wrap image data
    image = zbar.Image(width, height, 'Y800', raw)

    # scan the image for barcodes
    scanner.scan(image)

    # extract results
    for symbol in image:
        # do something useful with results
        print 'decoded', symbol.type, 'symbol', '"%s"' % symbol.data

    # clean up
    del(image)
    return symbol.data

PIN = 18
GPIO.setmode(GPIO.BCM)#set GPIO pin number
GPIO.setup(PIN, GPIO.IN)

while True:
    if GPIO.input(PIN):
        codenum = getbarcode();
        print '"%s"' % codenum
