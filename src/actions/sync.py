import sys
import time
import subprocess
from ui import clear_screen, read_key

def git_fetch():
    
    subprocess.run(["git", "fetch"])
    
def git_status():
    
    result = subprocess.run(
        ["git", "status"],
        text=True,
        capture_output=True
    )
    print(result.stdout)
    
    print("\n[home]  [s]-push [l]-pull", end="", flush=True)

def git_push():

    subprocess.run(["git", "add", "."])
    subprocess.run(["git", "commit", "-m", "upd"])
    subprocess.run(["git", "push"])
    
    print("\n[home] ", end="", flush=True)
    read_key()
    
def git_pull():
    
    subprocess.run(["git", "pull"])
    
    print("\n[home] ", end="", flush=True)
    read_key()

def run():
    
    clear_screen()
    git_fetch()
    git_status()
    
    choice = read_key().lower()

    if choice == "s":

        clear_screen()
        git_push()
        
    elif choice == "l":
        
        clear_screen()
        git_pull()
