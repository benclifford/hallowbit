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
 for count in range(0,10): 
  colour = random_colour()
  for row in range(0,5):
    for col in range(0,5):
      set_np(row,col,colour)
    np.show()
    sleep(300)
    for col in range(0,5):
      set_np(row,col,(0,0,0))
    np.show()


def set_vrows():
 np[0] = (255,255,255)
 for count in range(0,10): 
  colour = random_colour()
  for row in range(0,5):
    for col in range(0,5):
      set_np(col,row,colour)
    np.show()
    sleep(300)
    for col in range(0,5):
      set_np(col,row,(0,0,0))
    np.show()

def set_xrows():
 np[0] = (255,255,255)
 for count in range(0,10): 
  colour = random_colour()
  xcol = random.randint(0,4)
  ycol = random.randint(0,4)
  for row in range(0,5):
    set_np(row,ycol,colour)
  for col in range(0,5):
    set_np(xcol,col,colour)
  np.show()
  sleep(600)
  for row in range(0,5):
    set_np(row,ycol,(0,0,0))
  for col in range(0,5):
    set_np(xcol,col,(0,0,0))


while True:
  c = random.randint(0,2)
  # c = 2
  if c == 0:
    set_hrows()
  if c == 1:
    set_vrows()
  if c == 2:
    set_xrows()

