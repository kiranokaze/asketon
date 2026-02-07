import ui
from actions import sync, workout, version, menu, tasks

ACTIONS = {
    "v": version.run,
    "s": sync.run,
    "w": workout.run,
    "t": tasks.run
}
        
def run():

    while True:
        
        ui.clear_screen()
        menu.run()

        key = ui.read_key().lower()
            
        if key == "q":
            ui.clear_screen()
            ui.quit()
            break
            
        action = ACTIONS.get(key)
        if action:
            ui.clear_screen()
            action()

if __name__ == "__main__":
    run()
