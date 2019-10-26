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

## 2018-10-23

Had 7 pixels sewn by bedtime last night - did 3 more when I woke up,
improving my sewing technique (I hope) so that I'm getting much
faster: using a single bus thread for power rails rather than
a separate thread per pixel, and using one long thread and cutting
it as I sew, rather than cutting 5 inch sections first and sewing
them individually (and yes, I'm using inches as the units of
measure for this project).

All 10 pixels flash RGB in sequence using neoflasher.py - so the
electrical connections are in place a bit.

Apparently this setup will be washable!
https://learn.adafruit.com/washing-wearable-electronics/hand-wash

And in the evening, up to 20 LEDs. The last two weren't working but
I snipped away from excess conductive thread and stretched and
wiggled it and they started working. Which is not a very
satisfying explanation.

** 2018-10-24

Off to B&Q to buy some speaker cable to attach 4 wrist-buttons back up to
the microbit which I expect to be nearer my torso. (GBP 4 for 10 metres
- this bit is measuring in SI not Imperial)

Rule of thumb for thread length: use twice as much as the distance I'm
expecting to trace - for long runs. and for between pixels on the
same row: at least 3x

Rule of thumb: easier to sew next pixel Data In pad first, and then
sew back to previous Data Out.

All 25 pixels sewn in. Writing (2,2,2) to all pixels, i can visually
see drop in brightness along the powersnake: at the end the blue
LED isn't even visible at 2,2,2. On the + rail, between the leg of the
smooth capactitor near the start, and the final bit of + thread at the
end of the snake, I can see a voltage drop of about 0.25v
and 0.36v on the negative rail. I think + is less of a drop because 
I have an extra crossconnect on one turn.

Added a longer cross connect - from the two outer turns of the 
+ rail, and got the end to capacitor voltages drop to 0.17v (from 0.25v)

This is with a supply voltage, from the microbit, of 3.15v (measured
across the capactor).

After sewing in a negative rail cross connect, right from the start
to the final curve (so sort of mirroring rotationally the
+ve cross connect), I now see a voltage across the end terminals
of 2.95v vs a capacitor voltages of 3.15v

But that final pixel isn't the dimmest now!

The lowest voltage i can find, measuring across pads, is 2.90v
sort of in the middle near curves, probably as the total distance
is getting long.

Anyway for this supply setup, where I don't want to draw too much
power from the microbit, this is ok.

If I illuminate more, I expect more voltage drop...

Looks like maybe I can make the LEDs 10x as bright as they are
now (20,20,20) and fit within power budget of 90mA. To my eye,
the first two or three LEDs up by the power connector are
noticeably whiter than all the others which are redder.

With (20,20,20), voltages are:

capacitor: 3.12v

At end of tail: 2.85v

Worst drop across an individual pixel: 2.76v

voltage drop across cross connects: 0.3v (+ve) and 0.6v (-ve)

### Bigger power supply

I'm now going to move to something more like the power supply
I want to use when I'm wearing this:  a USB battery will supply 
the microbit out of one port, and directly supply 5v to the power
bus of the neopixels out of another port.

There's a trick with an extra pixel and a diode to build a hacky
level convertor, which I'm going to try now.
https://hackaday.com/2017/01/20/cheating-at-5v-ws2812-control-to-use-a-3-3v-data-line/

I'll need a USB cable to get a connector from, but I have a few
of those from poundland.

Also make snake program I wrote the other day display on both the microbit (with brightness control) and neopixel matrix (with colour control)

### 2018-10-25

Didn't get round to doing that power supply stuff yesterday.

This morning soldering buttons - with the buttons in place,
I'll have usable hardware as long as I don't light the LEDs up
too brightly, so that unlocks more potential.

Which pins to use?

It's a jumble of "you can use any pin" vs "other functionality which might interfere (eg LEDs, i2c)"

the obvious pins are 0 1 2 - the big ones.

I'm already using 0 for the neopixel.

8,16 look to behave the same.

so:

0  neopixel

1  button blue

2
8
16

I'll use 0v on the other side of the switch so need to set
pullup mode on the button.

the docs say 0,1,2 have external pullsups, so pullup mode is what
i wants anyway...

set_pull is not very documented. - see microbit/micropython PR #382


on a practical note, I'm going to stay somewhere else from today until
the halloween party that I want this for - so I need to pack up the
things I think I will need into a small bag, and hope I've got everything.

===
later, in pub:
showed to some people, powering it off battery for the first time.
unfortunately the battery kept shutting down. that was frustrating.
it happened 2y ago with different usb battery though - so unsurprising,
though interestingly this was doing it per-port - it shut down the
microbit port while still charging two phones.

I solved it then by putting a resistor across the power lines of the
USB, on a second port. It looks like i'd have to do it on the same
port here.

But someone on
https://forum.pjrc.com/threads/28624-USB-Battery-Bank-Prevent-Shut-Down
points out that the current draw might only need to happen every so 
often (eg a 0.1s pulse every 5s is what someone thinks might work, someone
else says 0.2s)

I'm going to have an extra neopixel for doing level conversion so maybe
I can make sure I power that periodically to full brightness.


https://forum.pjrc.com/threads/28624-USB-Battery-Bank-Prevent-Shut-Down

## 2018-10-27

sew on microbit edge connector PCB - microbit upside down looks like
it will take the weight better.

soldering onto PCB - decided to use the pcb tracks on microbit
edge connector board:

one for 5v, one for 4.5v, one for resistor-protected pin0 

abandon buttons for tonight due to time

one LED at 100% is not enough to keep power on.

one at 255,255,255 + 25 x (4,4,4) is enough

if assume that is linear in power consumption, then that means 
two or three at full power should be enough

### at the party

got it all wired up. got some patterns made - used snake game, and
four different intense colour based patterns.

people liked it

with enough LEDs on in these patterns, it didn't switch off

the sewing was a bit glitch-causing but that kinda made it look
cool


## 2019-10-25

A year's passed and I have less than 24h to pick up this project and finish
it for *this* year's halloween...

Let's see how useful these notes are.

The tshirt with microbit in it won't boot, but microbit powered from its
own USB will work. Time to get the multimeter out. Realised I need to
connect separate power line for the microbit - it doesn't draw from the
docking connector (not sure why?). Now it flashes a bunch of LEDs but there
is a loose control connection half way through the grid which causes the
bottom pixels to not light... holding it down with finger makes the whole
array work - so this maybe just needs some glue?

The microbit was still loaded up with the software from last year!
so software-wise it worked as soon as I got the wiring fixed.

## 2019-10-26

Used a bit of solder to fix up the missing loose connection - the solder
won't stick to the thread itself but it does stick to the metal pads on
the neopixels, and holds stuff a little more in place. Hopefully that's
good enough for today.

Let's try loading the software from this repo onto the microbit again,
using uflash. A bit of messing round with the wrong usb cable and
mountpoints, but this command worked: sudo uflash ./hallow.py /media/tmp

Did a bit of fiddling with snake colouring to make the body topology
more visible when the display is getting full.

Now it's time to attach some buttons.

I'd also like mypy to work to tell me errors before I load them on and have
to read exception messages off the 5x5 scrollng display... but let's not
get distracted from the hardware side for now.

I realised I can have the microbit USB connected into laptop for programming
while also powering the pixel array from the t-shirt USB connector... maybe
that's why I gave them separate connectors?

There are lots of pins on the microbit, but they're used for lots of
purposes: https://microbit.org/guide/hardware/pins/
... so I need to figure out which ones I can use.

Looks like earlier in journal I wrote to use pins: 1,2,8,16, and that two
of those have pullups, so the buttons need to go down to 0v, not to +v.
This arrangement leaves the A/B buttons on the microbit board separately
connected so they could be used to select mode/game/etc...

Having pins on the breakout board is a bit annoying, rather than holes to
solder directly to -- for the one pin i've used already, I ended up chopping
off a bit of a jumper cable.  So I suppose I'll have to do something like
that here too.

After a bunch of soldering, let's test out the pins by uploading a test
program... I already have external-button.py!

Now attach the pins as follows:

red 1  [up]
green 2 [down]
blue 8 [left]
yellow 16  [right]

These will all need securing and taping a lot but lets get going on the
software...

First, modify snake to be controlled by buttons rather than th AI...
and as part of that do a refactor... and now I get a memory error
at boot...

is my 5kb source file too big? :(

I removed an unused function (set_one) and it runs without memory error
so I guess I am right on the limit of what fits?

There's also a minify option in uflash I should try out. looks like I need
to install 'nudatus'? seems to do something.



