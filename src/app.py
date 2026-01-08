from ui import read_key, clear_screen, clear_last_line
from actions import git, workout, about, diary, menu

ACTIONS = {
    "a": about.run,
    "g": git.run,
    "w": workout.run,
    "d": diary.run,
}
        
def run():
    
    clear_screen()
    menu.run()
    
    print("sync.. ",end="", flush=True)
    
    try:
        git.git_fetch()
        
        if git.has_remote_commits():
            git.git_pull()
            
    except Exception:
        pass
    
    clear_last_line()
    
    while True:
        
        print("enter the first letter.. ", end="", flush=True)
        key = read_key().lower()
            
        if key == "q":
            
            clear_last_line()
            print("sync.. ",end="", flush=True)
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
    