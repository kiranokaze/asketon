import sys
import subprocess
from ui import clear_screen, read_key

def run():
    
    print("fetching updates...")
    subprocess.run(["git", "fetch"], stdout=subprocess.DEVNULL)
    
    result = subprocess.run(
        ["git", "status"],
        text=True,
        capture_output=True
    )
    
    clear_screen()
    print(result.stdout)
    print("\n[home] [u]-push [d]-pull ", end="", flush=True)
    choice = read_key().lower()

    if choice == "u":
        clear_screen()
        subprocess.run(["git", "add", "."])
        subprocess.run(["git", "commit", "-m", "upd"])
        subprocess.run(["git", "push"])
        print("\n[home] ", end="", flush=True)
        read_key()
        
    elif choice == "d":
        clear_screen()
        subprocess.run(["git", "pull"])
        print("\n[enter] ", end="", flush=True)
        read_key()
        reboot()
