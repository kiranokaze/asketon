import sys
import time
from pathlib import Path
from ui import clear_screen
from actions import git
import subprocess

DATA_DIR = Path("data")
MAIN_FILE = DATA_DIR / "menu.txt"

def run():
    
    clear_screen()
    
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
