from microbit import *
import neopixel

neopixel_pin = pin0
neopixel_count = 26

np = neopixel.NeoPixel(neopixel_pin, neopixel_count)
np.clear()

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



set_one()

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
