# SPDX-License-Identifier: MIT
# -*- coding: utf-8 -*-

import math
import os
import digitalio
import board
import time
from adafruit_rgb_display.rgb import color565
import adafruit_rgb_display.st7789 as st7789
from PIL import Image, ImageDraw, ImageFont
from fonts.ttf import RobotoMedium


# Configuration for CS and DC pins for Raspberry Pi
cs_pin = digitalio.DigitalInOut(board.CE0)
dc_pin = digitalio.DigitalInOut(board.D25)
reset_pin = None
BAUDRATE = 64000000  # The pi can be very fast!
# Create the ST7789 display:
display = st7789.ST7789(
    board.SPI(),
    cs=cs_pin,
    dc=dc_pin,
    rst=reset_pin,
    baudrate=BAUDRATE,
    width=135,
    height=240,
    x_offset=53,
    y_offset=40,
)

FLIP = os.environ.get('FLIP', False)
WIDTH = display.height
HEIGHT = display.width
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
COLORS = [
    (255, 0, 0),
    (255, 128, 0),
    (255, 255, 0),
    (128, 255, 0),
    (0, 255, 0),
    (0, 255, 128),
    (0, 255, 255),
    (0, 128, 255),
    (0, 0, 255),
    (255, 0, 255),
    (255, 0, 128),
]
index = 0

font = ImageFont.truetype(RobotoMedium, 40)
img = Image.new("RGB", (WIDTH, HEIGHT), 0)
draw = ImageDraw.Draw(img)

def show_credits():
    global index
    ROTATION = 270 if FLIP else 90
    draw.rectangle((0, 0, WIDTH, HEIGHT), fill=BLACK)
    draw.text((int(WIDTH*0.09), int(HEIGHT*0.35)), "promethee", font=font, fill=COLORS[index])
    draw.text((int(WIDTH*0.2), int(HEIGHT*0.6)), "@github", font=font, fill=COLORS[index])
    display.image(img, ROTATION)

backlight = digitalio.DigitalInOut(board.D22)
backlight.switch_to_output()
backlight.value = True
buttonA = digitalio.DigitalInOut(board.D23)
buttonB = digitalio.DigitalInOut(board.D24)
buttonA.switch_to_input()
buttonB.switch_to_input()

paused = False

while True:
    if not buttonB.value:
        FLIP = not FLIP
        time.sleep(0.3)
    if not buttonA.value:
        paused = not paused
        time.sleep(0.3)
    if not paused:
        index = index + 1 if index < len(COLORS) - 1 else 0

    show_credits()
