from microbit import *
import neopixel

neopixel_pin = pin0
neopixel_count = 8

np = neopixel.NeoPixel(neopixel_pin, neopixel_count)
np.clear()

while True:
  np[0] = (255,0,0)
  np[1] = (0,0,0)
  np.show()
  display.scroll('x2.')
  sleep(500)
  np[0] = (0,0,0)
  np[1] = (0,255,0)
  np.show()
  sleep(1500)

