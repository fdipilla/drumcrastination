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
    
    if key == b'0':
        Popen(["paplay", "sounds/bop_kick_snares_off_1.ogg"])
    elif key == b'1':
        Popen(["paplay", "sounds/turn_snare_on_1.ogg"])
    elif key == b'2':
        Popen(["paplay", "sounds/turn_snare_on_2.ogg"])
    elif key == b'3':
        Popen(["paplay", "sounds/floor_tom_snares_on_4.ogg"])
    elif key == b'4':
        Popen(["paplay", "sounds/hihat_closed_2.ogg"])
    elif key == b'5':
        Popen(["paplay", "sounds/snare_snares_on_3.ogg"])
    elif key == b'6':
        Popen(["paplay", "sounds/hihat_close_5.ogg"])        
    elif key == b'7':
        Popen(["paplay", "sounds/flat_ride_6.ogg"])
    elif key == b'8':
        Popen(["paplay", "sounds/rack_tom_snares_off_2.ogg"])
    elif key == b'9':
        Popen(["paplay", "sounds/ride_2.ogg"])



