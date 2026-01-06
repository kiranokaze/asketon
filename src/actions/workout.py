from ui import clear_screen, read_key
from pathlib import Path
import tty

DATA_DIR = Path("data")

EXERCISES = {
	1: ("pullups", "pullups"),
	2: ("pushups", "pushups"),
	3: ("squats", "squats"),
}

def read_number(name: str) -> int:
	path = DATA_DIR / f"{name}.txt"
	if not path.exists():
		return 0
	return int(path.read_text().strip())

def write_number(name: str, value: int):
	path = DATA_DIR / f"{name}.txt"
	path.write_text(str(value))
		
def add_reps(key: str):
	name, label = EXERCISES[key]
	
	print("\n")
	print(f"how strong are you.. _{label.lower()} > ",end="", flush=True)

	value = input().strip()

	if not value.isdigit():
		return

	current = read_number(name)
	write_number(name, current + int(value))

def run():
	while True:
		
		for key, (name, label) in EXERCISES.items():
			value = read_number(name)
			print(f"{key} | {label} - {value}\n")

		print("\n[home] [1] [2] [3] ", end="", flush=True)

		choice = read_key().lower()
		
		if choice == "h":
			return
		
		try:
			choice = int(choice)
		except ValueError:
			key = None

		if choice in EXERCISES:
			add_reps(choice)
			
		clear_screen()
