#!/usr/bin/python
# -*- coding: UTF-8 -*-

import time
import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
from PIL import Image, ImageFont, ImageDraw
import StringIO
import pygame
import zipfile
import os, sys

# Ports used for fthe Display. You may have to change them to yours
RST = 25
DC = 24

SPI_PORT = 0
SPI_DEVICE = 0

# 128x64 display with hardware SPI:
disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST, dc=DC, spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE, max_speed_hz=16000000))

# Initialize library.
disp.begin()

# Clear display.
disp.clear()
disp.display()

# Get display width and height.
width = disp.width
height = disp.height

# Create image buffer.
# Make sure to create image with mode '1' for 1-bit color.
image = Image.new('1', (width, height))

# Load default font.
font = ImageFont.load_default()

# Create drawing object.
draw = ImageDraw.Draw(image)

# Display Loading status
def disp_status(msg):
    # Draw a black filled box to clear the image.
    draw.rectangle((0,0,width,height), outline=0, fill=0)
    draw.text((4, 16), "12864 SSD1306 Player", font=font, fill=255)
    draw.text((54, 30), "by xswxm.com", font=font, fill=255)
    draw.text((0, 54), msg, font=font, fill=255)
    # Display image.
    disp.image(image)
    disp.display()


# Load zip file
disp_status('Loaing ZIP file...')
file = sys.argv[1]
zfile = zipfile.ZipFile(file, 'r')

# Load FPS
disp_status('Loaing FPS...')
fps = int(zfile.read('fps'))

# Play music
disp_status('Loaing audio...')
pygame.init()
pygame.mixer.music.load(StringIO.StringIO(zfile.read('audio.ogg')))
pygame.mixer.music.play()

# Initialize time for starting display image
time_sta = time.time()

try:
    while True:
        # Current Time
        time_cur = time.time()
        # Calculate the right frame to display
        frame = int((time_cur - time_sta) * fps) + 1
        # Load image and convert to 1 bit color.
        # image = Image.open('/home/pi/badapple/BMP/ba' + str(frame) + '.bmp')
        image = Image.open(StringIO.StringIO(zfile.read('img' + str(frame) + '.bmp')))
        # print 'Frame: ' + str(frame)
        disp.image(image)
        disp.display()
except:
    # Clear Display
    disp.clear()
    disp.display()
