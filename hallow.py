from microbit import *
import neopixel

import random

neopixel_pin = pin0
neopixel_count = 26

np = neopixel.NeoPixel(neopixel_pin, neopixel_count)
np.clear()


def set_np(x,y,col):
  if y % 2 == 0:
    x = 4-x

  pixel = y * 5 + x + 1

  np[pixel] = col

def set_flat():
  while True:
    np[0] = (255,255,255)
    for led in range(1,neopixel_count):
      np[led] = (4,4,4)
    np.show()


def set_one():
  while True:
    np[0] = (255,255,255)
    for led in range(1,3):
      np[led] = (255,255,255)
    np.show()

def random_colour():
  r = random.randint(0,5)
  if r == 0:
    return (255,0,0)
  if r == 1:
    return (0,255,0)
  if r == 2:
    return (255,255,0)
  if r == 3:
    return (0,0,255)
  if r == 4:
    return (255,0,255)
  if r == 5:
    return (0,255,255)
  return(255,255,255)

def set_hrows():
  np[0] = (255,255,255)
  colour = random_colour()
  for row in range(0,5):
    for col in range(0,5):
      set_np(row,col,colour)
    np.show()
    sleep(300)
    for col in range(0,5):
      set_np(row,col,(0,0,0))
    np.show()

while True:
  set_hrows()

def foo():
  for led in range(1,neopixel_count):
    np[led] = (255,0,0)
    np.show()
    sleep(100)
    np[led] = (0,255,0)
    np.show()
    sleep(100)
    np[led] = (0,0,255)
    np.show()
    sleep(100)
    np[led] = (25,25,25)
    # np[led] = (64,64,64)
    np.show()