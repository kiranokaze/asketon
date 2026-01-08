from ui import read_key, clear_screen
from actions import git, workout, about, diary, menu

ACTIONS = {
    "a": about.run,
    "g": git.run,
    "w": workout.run,
    "d": diary.run,
}
        
def run():
    
    clear_screen()
    
    try:
        git.git_fetch()
        
        if git.has_remote_commits():
            git.git_pull()
            git.reboot()
            
    except Exception:
        pass
    
    while True:

        menu.run()
        key = read_key().lower()
        clear_screen()
            
        if key == "q":
            git.git_push()
            print("uploaded to github. ", end="", flush=True)
            time.sleep(0.2)
            clear_screen()
            break
            
        action = ACTIONS.get(key)
        if action:
            action()

if __name__ == "__main__":
    run()
    