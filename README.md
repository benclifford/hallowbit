## Microbit Halloween costume

## Journal

### 2018-10-17

Received components from pimoroni. Expensive but a small envelope:
- 25 (actually 28) sewable neopixels
- some diodes to do voltage drop trick for using 3.3v logic
- 4 x coloured arcade buttons

### building/installing code from command line

Software stack: Previously I've only programmed microbit with
fairly simple stuff using the web based editors, which generate
a .hex file online.

I want a local build system, though, for more serious stuff.

https://stackoverflow.com/questions/52691853/generating-micropython-python-code-hex-file-from-commandline

pointed me in the right direction for this.

```
$ virtualenv new
$ pip3 install uflash
$ uflash main.py
```

puts my simple main program onto the microbit.

I'm running this inside a docker container (as  I do with lots of
my laptop installations) and the following docker parameter was
useful for getting the microbit mount point to appear inside
a docker container:
`--mount type=bind,source=/media,target=/media,bind-propagation=rslave`

### adding neopixels

Add components:
- kiktronic Edge connector breakout board
- neopixel 8 pixel strip (onto which i have soldered pins for breadboard)
- 1000uF capacitor (for neopixel power lines)
- resistor (for neopixel data lines)  - 600 ohm

(Capactior and resistor as recommended in https://learn.adafruit.com/adafruit-neopixel-uberguide/best-practices - although I havent used on small
projects before. and I'm using 600 ohm because that's what I found,
rather than 300-500 as noted in text)

I have some 8 element neopixel strips (that I used for halloween a
couple of years ago) that will be more convenient for prototyping
basic neopixel interactions on breadboard than the sewable display.
I'll run those off the microbit power supply for now too, so I
expect I won't be able to drive too much.

Add recommended protection capacitor onto power rail. Probably not
needed at this scale but I'll put it in now so I don't have to
remember to add later.


I'll use pin 0 for the neopixel data line, so put the 600 ohm
resister there and jumper pin 0 across.

and add some sample code - use https://bbcmicrobitmicropython.readthedocs.io/en/latest/neopixel.html as reference

I made a type error in the code, and the python level type error
scrolls across the 5x5 screen at boot time. Which is pretty weird but better
than nothing.

Other than that, the library was straightforward to use - like
neopixel libraries that I've used elsewhere.

## 2018-10-21

Attempting to write a couple of simple python games - just using the
microbit on-board buttons and screen.

First, very basic A/B left/right simon game, with randomness using the
A/B buttons, and symbols A B on screen.


Next, start on a snake game - this will have L/R steering rather than
compass steering, because I only have two buttons - though the costume
version I think I'd rather have compass steering. Also prototyped a
noughts and crosses board layout (but no logic)


## 2018-10-22

Start sewing neopixels onto a tshirt. Had to rummage in mother's
sewing box for a needle with a big enough eye as none of my
needles were big enough. It took 2 hours to sew the first three.
I hope I get faster.
