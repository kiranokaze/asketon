import tty
import sys
import termios
import time

def clear_screen():
	
    sys.stdout.write("\033[H\033[2J")
    sys.stdout.flush()

def alt_screen_in():
    
    print("\033[?1049h\033[H", end="")
    
    sys.stdout.write("\033[?1000l\033[?1002l\033[?1003l\033[?1006l")
    sys.stdout.flush()

def alt_screen_out():
    
    print("\033[?1049l", end="")
    time.sleep(0.2)
	
def read_key():
    
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        char = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return char

