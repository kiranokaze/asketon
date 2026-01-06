import time
import tty
import termios
import sys
import subprocess
import os

def clear_screen():

    sys.stdout.write("\033[H\033[2J")
    sys.stdout.flush()
    
def reboot():
    os.execv(sys.executable, [sys.executable] + sys.argv)

def show_menu(menu_lines):

    for i, line in enumerate(menu_lines):
		
        if i == len(menu_lines) - 1:
            print(line, end="", flush=True)
            
        else:
            print(line)
            time.sleep(0.015) 

def get_char():
    
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        char = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return char

def about():
    
    for i in range(10):
        print("")
    print("     https://github.com/kiranokaze ", end="", flush=True)
        
    get_char()
    
def git():
    
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
    choice = get_char().lower()

    if choice == "u":
        clear_screen()
        subprocess.run(["git", "add", "."])
        subprocess.run(["git", "commit", "-m", "upd"])
        subprocess.run(["git", "push"])
        print("\n[home] ", end="", flush=True)
        get_char()
        
    elif choice == "d":
        clear_screen()
        subprocess.run(["git", "pull"])
        print("\n[restart] ", end="", flush=True)
        get_char()
        reboot()
        
def main():
    
    try:
        with open("menu.txt", "r", encoding="utf-8") as f:
            menu_lines = f.read().splitlines()
    except FileNotFoundError:
        menu_lines = ["no menu.txt file."]

    while True:

        clear_screen()

        show_menu(menu_lines)

        choice = get_char().lower()
		
        clear_screen()
        
        
        if choice == "a":
            about()
            
        elif choice == "g":
            git()
            
        elif choice == "q":
            time.sleep(0.5)
            break

if __name__ == "__main__":
    main()

