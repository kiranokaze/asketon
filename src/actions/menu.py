import time
from pathlib import Path
from ui import clear_screen

MAIN_FILE = Path("menu.txt")

def run():
    
    clear_screen()
    print("[a]", end="", flush=True)
    time.sleep(0.1)
    print("sketon")
    
    try:
        menu_lines = MAIN_FILE.read_text(encoding="utf-8").splitlines()
        
    except FileNotFoundError:
        menu_lines = ["no main_screen.txt file."]

    for i, line in enumerate(menu_lines):
		
        if i == len(menu_lines) - 1:
            print(line, end="", flush=True)
        else:
            print(line)
            time.sleep(0.02)
