from microbit import *
import random

import neopixel

neopixel_pin = pin0
neopixel_count = 25

np = neopixel.NeoPixel(neopixel_pin, neopixel_count)
np.clear()


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

def set_np(x,y,brightness):
  if y % 2 == 0:
    x = 4-x

  pixel = y * 5 + x

  np[pixel] = (25 - brightness,brightness * 2,0)
    

def random_start_pos():
  # avoid starting at an edge, so that we don't
  # immediately crash
  return [(random.randint(1,3), random.randint(1,3))]

snake_dir = (0,1)
snake = random_start_pos()

target_len = 2

counts = 0

while True:

  display.clear()

  for p in range(0,neopixel_count):
    np[p] = (0,0,0)

  brightness = 9
  for (x,y) in list(reversed(snake)):
    display.set_pixel(x,y,brightness)
    set_np(x,y,brightness)
    if brightness > 5:
      brightness = brightness - 1
  np.show()

  sleep(500)

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

  # this is the environment checking crashes
  if will_crash(snake, snake_dir):
    sleep(2000)
    target_len = 2
    snake_dir = (0,1)
    snake = random_start_pos()

  (head_x,head_y) = snake[-1] 
  (dx,dy) = snake_dir

  snake.append( (head_x + dx, head_y + dy) ) # new head

  if len(snake) > target_len:
    snake.pop(0) # old tail

  counts = counts + 1

  if counts > 5:
    counts = 0
    target_len = target_len + 1

