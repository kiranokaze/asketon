from ui import read_key, clear_screen, clear_last_line
from actions import git, workout, about, diary, menu
from update import update

ACTIONS = {
    "a": about.run,
    "g": git.run,
    "w": workout.run,
    "d": diary.run,
}
        
def run():
    
    clear_screen()
    menu.run()
    
    update()
    
    while True:
        
        print("› ", end="", flush=True)
        key = read_key().lower()
            
        if key == "q":
            
            git.git_push()
            clear_screen()
            break
            
        action = ACTIONS.get(key)
        if action:
            clear_screen()
            action()
            
        menu.run()

if __name__ == "__main__":
    run()
