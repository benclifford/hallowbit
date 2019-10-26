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
def will_crash(snek, snek_dir):
  (head_x,head_y) = snek[-1] 
  (dx,dy) = snek_dir

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

  for (x,y) in snek:
    if x == next_x and y == next_y:
      return True

  return False

def snek(ai):
  np.clear()
  snek_dir = (0,1)
  snek = [(random.randint(1,3), random.randint(1,3))]
  target_len = 3 
  counts = 0
  go = True
  while go:

    display.clear()

    np[0] = (255,255,255)
    for p in range(1,26):
      np[p] = (0,0,0)

    brightness = 9
    for ((x,y),pos) in zip(list(reversed(snek)),range(0,5*5)):
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
        snek_dir = snek_ai(snek, snek_dir)
    else:
        sleep(500) # slower for humans
        snek_dir = snek_buttons(snek, snek_dir)

    if will_crash(snek, snek_dir):
      go = False
      for (x,y) in snek:
        set_np(x,y,(255,0,0))
      sleep(1000)
      np.clear()

    (head_x,head_y) = snek[-1] 
    (dx,dy) = snek_dir

    snek.append( (head_x + dx, head_y + dy) ) # new head
    if len(snek) > target_len:
      snek.pop(0) # old tail

    counts += 1
    if counts > 5:
      counts = 0
      target_len += 1

def snek_buttons(snek, snek_dir):
  if not pin1.read_digital():
    return (0,-1)
  if not pin2.read_digital():
    return (0,1)
  if not pin8.read_digital():
    return (-1,0)
  if not pin16.read_digital():
    return (1,0)
  return snek_dir

def snek_ai(snek, snek_dir): # snek autopilot
    random_change = random.randint(0,10) == 7

    if will_crash(snek, snek_dir) or random_change:
      (dx,dy) = snek_dir

      if dx == 0: # then we're going along the y axis, so could go up or down
        if not will_crash(snek, (1,0)):
          snek_dir = (1,0)
        elif not will_crash(snek, (-1,0)):
          snek_dir = (-1,0)
        # if neither works, give up...
      elif dy == 0: # then we're going along the x axis
        if not will_crash(snek, (0,1)):
          snek_dir = (0,1)
        elif not will_crash(snek, (0,-1)):
          snek_dir = (0,-1)

    return snek_dir

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
    snek(True)
  if c == 4:
    set_rainbow()
  if c == 5:
    set_zoomout()

 while pin11.read_digital():
   snek(False)
