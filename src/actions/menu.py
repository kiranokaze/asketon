import time
from pathlib import Path
from ui import clear_screen

MAIN_FILE = Path("menu.txt")

def run():
    
	clear_screen()
	print("[a]", end="", flush=True)
	time.sleep(0.2)
	print("sketon\n\n")
	time.sleep(0.02)
	print("[finance] [tasks] [workout]\n")
	time.sleep(0.02)
	print("[sync] [ver] [quit]\n\n")
	time.sleep(0.02)
	print("> ", end="", flush=True)
