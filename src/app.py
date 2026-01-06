import time
import tty
import termios
import sys
import subprocess

def clear_screen():

    sys.stdout.write("\033[H\033[2J")
    sys.stdout.flush()

def power_off():
    
    progress = ["/// ", "//  ", "/   ", "    "]
    for line in progress:
        clear_screen()
        print(line, end="", flush=True)
        time.sleep(0.1)
        clear_screen()
        
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
    
    result = subprocess.run(
        ["git", "status"],
        text=True,
        capture_output=True
    )
    print(result.stdout)
    
    print("\n[home] [p]-push [l]-pull ", end="", flush=True)
    choice = get_char().lower()

    if choice == "p":
        clear_screen()
        subprocess.run(["git", "add", "."])
        subprocess.run(["git", "commit", "-m", "upd"])
        subprocess.run(["git", "push"])
        print("\n[home] ", end="", flush=True)
        get_char()
        
    elif choice == "l":
        clear_screen()
        subprocess.run(["git", "pull"])
        print("\n[home] ", end="", flush=True)
        get_char()
        
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
            power_off()
            break

if __name__ == "__main__":
    main()

