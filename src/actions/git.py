import sys
import time
import subprocess
from ui import clear_screen, read_key, clear_last_line

def git_fetch():
    
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

def has_local_changes() -> bool:
    
    result = subprocess.run(
        ["git", "status", "--porcelain"],
        capture_output=True,
        text=True
    )
    return bool(result.stdout.strip())

def git_push():
    
    if not has_local_changes():
        return
        
    clear_last_line()
    print("..", end="", flush=True)
    
    subprocess.run(["git", "add", "."])
    subprocess.run(
        ["git", "commit", "-m", "upd"],
        stdout=subprocess.DEVNULL
    )
    subprocess.run(
        ["git", "push"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )
    
def git_pull():
    
    subprrocess.run(
        ["git", "pull"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )
    
def run():
    
    clear_screen()
    git_status()
    
    print("\n[home]  [p]-push ", end="", flush=True)
    choice = read_key().lower()

    if choice == "p":

        clear_screen()
        git_push()
        clear_screen()
