import sys
import time
from pathlib import Path

DATA_DIR = Path("data")
MAIN_FILE = DATA_DIR / "main_screen.txt"

def run():
    
    sys.stdout.write("\033[H\033[2J")
    sys.stdout.flush()
    
    try:
        menu_lines = MAIN_FILE.read_text(encoding="utf-8").splitlines()
        
    except FileNotFoundError:
        menu_lines = ["no main_screen.txt file."]

    for i, line in enumerate(menu_lines):
		
        if i == len(menu_lines) - 1:
            print(line, end="", flush=True)
            
        else:
            print(line)
            time.sleep(0.015) 