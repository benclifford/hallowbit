
from microbit import *

pin1.set_pull(pin1.PULL_UP)
pin2.set_pull(pin2.PULL_UP)
pin8.set_pull(pin8.PULL_UP)
pin16.set_pull(pin16.PULL_UP)

while True:
  if not pin1.read_digital():
    display.scroll("1")
  if not pin2.read_digital():
    display.scroll("2")
  if not pin8.read_digital():
    display.scroll("8")
  if not pin16.read_digital():
    display.scroll("X")
  display.scroll(".")


