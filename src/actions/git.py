import sys
import subprocess
from ui import clear_screen, read_key

def git_fetch():
    
    clear_screen()
    
    print("fetching updates.. ", end="", flush=True)
    
    subprocess.run(["git", "fetch"], stdout=subprocess.DEVNULL)
    
    clear_screen()
    
def git_status():
    
    result = subprocess.run(
        ["git", "status"],
        text=True,
        capture_output=True
    )
    
    print(result.stdout)
    
def git_push():
    
    subprocess.run(["git", "add", "."])
    subprocess.run(["git", "commit", "-m", "upd"])
    subprocess.run(["git", "push"])
    
def git_pull():
    
        subprrocess.run(["git", "pull"])
    
def run():
    
    git_fetch()
    
    git_status()
    
    print("\n[home] [u]-push [d]-pull ", end="", flush=True)
    choice = read_key().lower()

    if choice == "u":
        
        clear_screen()
        git_push()
        print("\n[home] ", end="", flush=True)
        read_key()
        
    elif choice == "d":
        
        clear_screen()
        git_pull()
        print("\n[reboot] ", end="", flush=True)
        read_key()
        reboot()
