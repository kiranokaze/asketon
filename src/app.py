from ui import read_key, clear_screen, clear_last_line
from actions import sync, body, version, diary, menu

ACTIONS = {
    "v": version.run,
    "s": sync.run,
    "b": body.run,
    "d": diary.run,
}
        
def run():
    
    clear_screen()
    menu.run()
    
    while True:

        key = read_key().lower()
            
        if key == "q":
            clear_screen()
            break
            
        action = ACTIONS.get(key)
        if action:
            clear_screen()
            action()
            
        menu.run()

if __name__ == "__main__":
    run()
