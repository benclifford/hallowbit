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


def set_zoomout():
 for count in range(0,3):
  colour = random_colour()
  for radius in range(0,4):
    for row in range(0,5):
      for col in range(0,5):
        if abs(row - 2) + abs(col - 2) == radius:
          set_np(row, col, colour)
    np[0] = (255,255,255)
    np.show()
    sleep(300)
    for p in range(1,neopixel_count):
      np[p] = (0,0,0)
  np.clear()
  

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

def set_rows(hv):
 np[0] = (255,255,255)
 for count in range(0,10): 
  colour = random_colour()
  for row in range(0,5):
    for col in range(0,5):
      if hv:
        set_np(row,col,colour)
      else:
        set_np(col,row,colour)
    np.show()
    sleep(300)
    for col in range(0,5):
      set_np(row,col,(0,0,0))
    np.show()


def set_rainbow():
  np[0] = (255,255,255)
  for count in range(0,50):
    for row in range(0,5):
      for col in range(0,5):
        set_np(row,col,random_colour())
    np.show()
    sleep(100) 
  np.clear()

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



# tells us whether the snake will crash
# on the next move.
def will_crash(snake, snake_dir):
  (head_x,head_y) = snake[-1] 
  (dx,dy) = snake_dir

  next_x = head_x + dx
  next_y = head_y + dy

  if next_x > 4:
    return True

  if next_x < 0:
    return True

  if next_y > 4:
    return True

  if next_y < 0:
    return True

  for (x,y) in snake:
    if x == next_x and y == next_y:
      return True

  return False


def random_start_pos():
  # avoid starting at an edge, so that we don't
  # immediately crash
  return [(random.randint(1,3), random.randint(1,3))]

def run_snake(ai):
  np.clear()

  snake_dir = (0,1)
  snake = random_start_pos()

  target_len = 3 

  counts = 0

  go = True
  while go:

    display.clear()

    np[0] = (255,255,255)
    for p in range(1,neopixel_count):
      np[p] = (0,0,0)

    brightness = 9
    for ((x,y),pos) in zip(list(reversed(snake)),range(0,5*5)):
      display.set_pixel(x,y,brightness)
      if pos < 2: # head
        set_np(x,y,(10 * brightness, 8 * brightness, 27 * brightness))
      else:
        shading = min(pos,26) # start read, head to green, via yellow
        set_np(x,y,((26-shading) * brightness, shading * brightness, 0))
      if brightness > 4:
        brightness = brightness - 1
    np.show()

    sleep(200)

    if ai:
        snake_dir = snake_ai(snake, snake_dir)

    # this is the environment checking crashes
    if will_crash(snake, snake_dir):
      go = False
      sleep(1000)
      np.clear()

    (head_x,head_y) = snake[-1] 
    (dx,dy) = snake_dir

    snake.append( (head_x + dx, head_y + dy) ) # new head

    if len(snake) > target_len:
      snake.pop(0) # old tail

    counts = counts + 1

    if counts > 5:
      counts = 0
      target_len = target_len + 1

def snake_ai(snake, snake_dir):

    # this is the autopilot checking if it will crash
    # it is allowed to go wrong, just like a player is
    # allowed to go wrong

    # are we forced to change direction by imminent crash?
    # or, should we change direction randomly anyway?
    # (in that second case, the path of not changing direction
    # if we'd crash on either of our alternatives keeps us
    # going rather than randomly turning to death)

    random_change = random.randint(0,10) == 7

    if will_crash(snake, snake_dir) or random_change:
      # We'd better take some evasive action to
      # not crash.
      # We have a choice of directions - usually two
      # and we can check if either of them is any good
      # and if so, take one of the good ones. 
    
      # assume we're going one of the 4 cardinal
      # directions

      (dx,dy) = snake_dir

      if dx == 0: # then we're going along the y axis
                  # and are possible positions are along
                  # the x axis

        if not will_crash(snake, (1,0)):
          snake_dir = (1,0)
        elif not will_crash(snake, (-1,0)):
          snake_dir = (-1,0)
        # if neither works, give up...

      elif dy == 0:
        if not will_crash(snake, (0,1)):
          snake_dir = (0,1)
        elif not will_crash(snake, (0,-1)):
          snake_dir = (0,-1)

    return snake_dir


while True:
  c = random.randint(0,5)
  # c = 5
  if c == 0:
    set_rows(False)
  if c == 1:
    set_rows(True)
  if c == 2:
    set_xrows()
  if c == 3:
    run_snake(True)
  if c == 4:
    set_rainbow()
  if c == 5:
    set_zoomout()
