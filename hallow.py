from microbit import *
import neopixel
import random

np = neopixel.NeoPixel(pin0, 26)
np.clear()

for p in [pin1, pin2, pin5, pin8, pin11, pin16]:
  p.set_pull(p.PULL_UP)

def set_np(x,y,col):
  if y % 2 == 0:
    x = 4-x
  pixel = y * 5 + x + 1
  np[pixel] = col

def set_zoomout():
 for count in range(0,3):
  colour = rand_color()
  for radius in range(0,4):
    for row in range(0,5):
      for col in range(0,5):
        if abs(row - 2) + abs(col - 2) == radius:
          set_np(row, col, colour)
    np[0] = (255,255,255)
    np.show()
    sleep(300)
    for p in range(1,26):
      np[p] = (0,0,0)
  np.clear()

def rand_color():
  cols = [
    (255,0,0),
    (0,255,0),
    (255,255,0),
    (0,0,255),
    (255,0,255),
    (0,255,255),
    (255,255,255)
  ]
  return cols[random.randint(0,5)]

def set_rows(hv):
 np[0] = (255,255,255)
 for count in range(0,10): 
  colour = rand_color()
  for row in range(0,5):
    for col in range(0,5):
      if hv:
        set_np(row,col,colour)
      else:
        set_np(col,row,colour)
    np.show()
    sleep(300)
    for col in range(0,5):
      if hv:
        set_np(row,col,(0,0,0))
      else:
        set_np(col,row,(0,0,0))
    np.show()

def set_rainbow():
  np[0] = (255,255,255)
  for count in range(0,50):
    for row in range(0,5):
      for col in range(0,5):
        set_np(row,col,rand_color())
    np.show()
    sleep(100) 
  np.clear()

def set_xrows():
 np[0] = (255,255,255)
 for count in range(0,10): 
  colour = rand_color()
  xcol = random.randint(0,4)
  ycol = random.randint(0,4)
  for n in range(0,5):
    set_np(n,ycol,colour)
    set_np(xcol,n,colour)
  np.show()
  sleep(600)
  for n in range(0,5):
    set_np(n,ycol,(0,0,0))
    set_np(xcol,n,(0,0,0))

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

def snake(ai):
  np.clear()
  snake_dir = (0,1)
  snake = [(random.randint(1,3), random.randint(1,3))]
  target_len = 3 
  counts = 0
  go = True
  while go:

    display.clear()

    np[0] = (255,255,255)
    for p in range(1,26):
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
        brightness -= 1
    np.show()

    if ai:
        sleep(200)
        snake_dir = snake_ai(snake, snake_dir)
    else:
        sleep(500) # slower for humans
        snake_dir = snake_buttons(snake, snake_dir)

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

    counts += 1
    if counts > 5:
      counts = 0
      target_len += 1

def snake_buttons(snake, snake_dir):
  if not pin1.read_digital():
    return (0,-1)
  if not pin2.read_digital():
    return (0,1)
  if not pin8.read_digital():
    return (-1,0)
  if not pin16.read_digital():
    return (1,0)
  return snake_dir

def snake_ai(snake, snake_dir): # snake autopilot
    random_change = random.randint(0,10) == 7

    if will_crash(snake, snake_dir) or random_change:
      (dx,dy) = snake_dir

      if dx == 0: # then we're going along the y axis, so could go up or down
        if not will_crash(snake, (1,0)):
          snake_dir = (1,0)
        elif not will_crash(snake, (-1,0)):
          snake_dir = (-1,0)
        # if neither works, give up...
      elif dy == 0: # then we're going along the x axis
        if not will_crash(snake, (0,1)):
          snake_dir = (0,1)
        elif not will_crash(snake, (0,-1)):
          snake_dir = (0,-1)

    return snake_dir

while True:

 while pin5.read_digital():
  c = random.randint(0,5)
  if c == 0:
    set_rows(False)
  if c == 1:
    set_rows(True)
  if c == 2:
    set_xrows()
  if c == 3:
    snake(True)
  if c == 4:
    set_rainbow()
  if c == 5:
    set_zoomout()

 while pin11.read_digital():
   snake(False)
