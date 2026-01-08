import os
import sys
import subprocess
from ui import clear_screen, read_key

def git_fetch():
    
    print("fetching updates.. ", end="", flush=True)
    
    subprocess.run(
        ["git", "fetch"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )
    
def git_status():
    
    result = subprocess.run(
        ["git", "status"],
        text=True,
        capture_output=True
    )
    print(result.stdout)
    
def has_remote_commits() -> bool:
    
    result = subprocess.run(
        ["git", "status"],
        text=True,
        capture_output=True
    )
    return "behind" in result.stdout

def git_push():
    
    subprocess.run(["git", "add", "."])
    subprocess.run(["git", "commit", "-m", "upd"])
    subprocess.run(["git", "push"])

    print("uploaded to github. ", end="", flush=True)
    time.sleep(0.2)
    clear_screen()
    
def git_pull():
    
    print("\nupdating.. ", end="", flush=True)
    subprrocess.run(["git", "pull"])
        
def reboot():
    
    os.execv(sys.executable, [sys.executable] + sys.argv)
    
def run():
    
    clear_screen()
    git_status()
    
    print("\n[home] [p]-push ", end="", flush=True)
    choice = read_key().lower()

    if choice == "p":
        
        clear_screen()
        git_push()
        print("\n[home] ", end="", flush=True)
        read_key()
