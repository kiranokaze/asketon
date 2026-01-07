import sys
import os
from ui import read_key, clear_screen
from actions import git, workout, about, diary, menu

ACTIONS = {
    "a": about.run,
    "g": git.run,
    "w": workout.run,
    "d": diary.run,
}

def reboot():
    
    os.execv(sys.executable, [sys.executable] + sys.argv)
        
def run():
    
    while True:

        menu.run()
        key = read_key().lower()
        clear_screen()
            
        if key == "q":
            break
            
        action = ACTIONS.get(key)
        if action:
            action()

if __name__ == "__main__":
    run()
    