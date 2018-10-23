from microbit import *
import neopixel

neopixel_pin = pin0
neopixel_count = 15

np = neopixel.NeoPixel(neopixel_pin, neopixel_count)
np.clear()

while True:
  for led in range(0,neopixel_count):
    np[led] = (255,0,0)
    np.show()
    sleep(100)
    np[led] = (0,255,0)
    np.show()
    sleep(100)
    np[led] = (0,0,255)
    np.show()
    sleep(100)
    np[led] = (0,0,0)
    np.show()
