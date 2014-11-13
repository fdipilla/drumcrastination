import termios, sys, os
from subprocess import Popen

TERMIOS = termios

def getkey():
    fd = sys.stdin.fileno()
    old = termios.tcgetattr(fd)
    new = termios.tcgetattr(fd)
    new[3] = new[3] & ~TERMIOS.ICANON & ~TERMIOS.ECHO
    new[6][TERMIOS.VMIN] = 1
    new[6][TERMIOS.VTIME] = 0
    termios.tcsetattr(fd, TERMIOS.TCSANOW, new)
    c = None
    try:
        c = os.read(fd, 1)
    finally:
        termios.tcsetattr(fd, TERMIOS.TCSAFLUSH, old)
    return c

while True:
    key = getkey()
    print(key)
    
    if key == b'n':
        Popen(["paplay", "sounds/drum_0.wav"])
    elif key == b'j':
        Popen(["paplay", "sounds/snare_1.wav"])
    elif key == b'a':
        Popen(["paplay", "sounds/snare_0.wav"])
