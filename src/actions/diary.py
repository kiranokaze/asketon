from ui import read_key, clear_screen
from pathlib import Path
import subprocess
from datetime import datetime, timedelta

DATA_DIR = Path("data")
DIARY_FILE = DATA_DIR / "diary.txt"

def view_diary():
	print("\n" * 20)
	if DIARY_FILE.exists():
		print(DIARY_FILE.read_text())
	else:
		print("diary is empty.")
	
def add_entry():
	print ("upload to my tech diary:\n")
	print("[leave empty to cancel]\n")
	text = input("> ").strip()
	
	if text == "":
		return
		
	now = datetime.utcnow() + timedelta(hours=4)
	timestamp = now.strftime("[ %d.%m.%y - %H:%M ]")
	
	with DIARY_FILE.open("a") as f:
		f.write(f"{timestamp}\n{text}\n\n")
	
def edit_entry():
	if not DIARY_FILE.exists():
		DIARY_FILE.touch()
	subprocess.run(["nano", "+{}".format(DIARY_FILE.read_text().count("\n") + 1), str(DIARY_FILE)])
	
def run():
	while True:
		clear_screen()
		view_diary()
		
		print("[home]  [add] [edit] ", end="", flush=True)
		choice = read_key().lower()
		clear_screen()
		
		if choice == "h":
			break
		elif choice == "a":
			add_entry()
		elif choice == "e":
			edit_entry()
