import tty
import sys
import termios
import time

def clear_screen():
	
    sys.stdout.write("\033[H\033[2J")
    sys.stdout.flush()
    
def quit():
	
	time.sleep(0.1)
	
def read_key():
    
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        char = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return char

