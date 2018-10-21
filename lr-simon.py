# left/right simon game

from microbit import *
import random

display.scroll("SIMON /")

level = 5

display.scroll("LEVEL {} /".format(level))

# TODO: generate this randomly, as long as
# `level` says we should make it

sequence = []

for n in range(0, level):

  r = random.randint(1,2)
  sequence.append(r)

# play sequence

def put_sym(symbol):
  if symbol == 1:
    display.scroll("A")
  elif symbol == 2: 
    display.scroll("B")
  else:
    display.scroll("?")

for symbol in sequence:
  put_sym(symbol)

# wait for sequence input

for symbol in sequence:
  # wait for exactly the given symbol input
  # and die if we get a different symbol input

  # TODO: input symbol
  inp = None
  while inp is None:
    if button_a.is_pressed():
      inp = 1
    elif button_b.is_pressed():
      inp = 2

  put_sym(symbol)

  if inp != symbol:
    display.scroll("XXX")
    # what lose/halt behaviour should happen?
    while True:
      pass


display.scroll("!!!WIN!!!")

#while True:
#  if button_a.is_pressed():
#    display.scroll('A')
#  if button_b.is_pressed():
#    display.scroll('B')


