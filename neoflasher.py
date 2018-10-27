from microbit import *
import neopixel

neopixel_pin = pin0
neopixel_count = 26

np = neopixel.NeoPixel(neopixel_pin, neopixel_count)
np.clear()

while True:
  np[0] = (255,255,255)
  for led in range(1,neopixel_count):
    np[led] = (8,8,8)
  np.show()

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
