from microbit import *

snake_dir = (0,1)

snake = [(2,1), (2,2)]

target_len = 3

counts = 0

while True:

  display.clear()

  brightness = 9
  for (x,y) in list(reversed(snake)):
    display.set_pixel(x,y,brightness)
    if brightness > 5:
      brightness = brightness - 1

  sleep(500)

  # change direction?
  # autopilot for now
  (head_x,head_y) = snake[-1] 
  (dx,dy) = snake_dir

  if head_y == 4 and head_x < 3 and dy > 0: 
    snake_dir = (1,0)
  elif head_y == 4 and head_x >= 3 and dy > 0: 
    snake_dir = (-1,0)
  elif head_x == 4 and head_y < 3 and dx > 0:
    snake_dir = (0,1)
  elif head_x == 4 and head_y > 3 and dx > 0:
    snake_dir = (0,-1)
  if head_y == 0 and head_x < 3 and dy < 0: 
    snake_dir = (1,0)
  elif head_y == 0 and head_x >= 3 and dy < 0: 
    snake_dir = (-1,0)
  elif head_x == 0 and head_y < 3 and dx < 0:
    snake_dir = (0,1)
  elif head_x == 0 and head_y > 3 and dx < 0:
    snake_dir = (0,-1)

  # reinitialise the direction, after motion changing
  (dx,dy) = snake_dir

  snake.append( (head_x + dx, head_y + dy) ) # new head

  if len(snake) > target_len:
    snake.pop(0) # old tail

  counts = counts + 1

  if counts > 5:
    counts = 0
    target_len = target_len + 1

