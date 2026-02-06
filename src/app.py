from ui import read_key, clear_screen, quit
from actions import sync, workout, version, menu

ACTIONS = {
    "v": version.run,
    "s": sync.run,
    "w": workout.run
}
        
def run():
    
    clear_screen()
    menu.run()
    
    while True:

        key = read_key().lower()
            
        if key == "q":
            clear_screen()
            quit()
            break
            
        action = ACTIONS.get(key)
        if action:
            clear_screen()
            action()
            
        menu.run()

if __name__ == "__main__":
    run()
