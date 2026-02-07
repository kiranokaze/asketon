import ui
from actions import sync, workout, version, menu

ACTIONS = {
    "v": version.run,
    "s": sync.run,
    "w": workout.run
}
        
def run():
    
    #ui.alt_screen_in()
    
    while True:
        
        menu.run()

        key = ui.read_key().lower()
            
        if key == "q":
            ui.clear_screen()
            #ui.alt_screen_out()
            break
            
        action = ACTIONS.get(key)
        if action:
            ui.clear_screen()
            action()

if __name__ == "__main__":
    run()
