## Microbit Halloween costume

## Journal

### 2018-10-17

Received components from pimoroni. Expensive but a small envelope:
- 25 (actually 28) sewable neopixels
- some diodes to do voltage drop trick for using 3.3v logic
- 4 x coloured arcade buttons

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

