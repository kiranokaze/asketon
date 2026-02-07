from pathlib import Path
from ui import clear_screen, read_key
from config import DB_PATH
import sqlite3

EXERCISES = {
	1: ("pullups", "pullups"),
	2: ("pushups", "pushups"),
	3: ("squats", "squats"),
}

def init_db():
	
	conn = sqlite3.connect(DB_PATH)
	conn.execute("""
		CREATE TABLE IF NOT EXISTS exercises (
			name TEXT PRIMARY KEY,
			count INTEGER DEFAULT 0
		)
	""")
	conn.commit()
	conn.close()
	
def view():
	
	for key, (name, label) in EXERCISES.items():
			value = read_number(name)
			print(f"{label} - {value}")
	print("\n[q] [1] [2] [3] ", end="", flush=True)
	
def read_number(name: str) -> int:
  
	conn = sqlite3.connect(DB_PATH)
	cursor = conn.execute("SELECT count FROM exercises WHERE name = ?", (name,))
	row = cursor.fetchone()
	conn.close()
	return row[0] if row else 0

def write_number(name: str, value: int):
	
	conn = sqlite3.connect(DB_PATH)
	conn.execute("INSERT OR REPLACE INTO exercises (name, count) VALUES (?, ?)", (name, value))
	conn.commit()
	conn.close()

def add_reps(choice_key: int):
	
	name, label = EXERCISES[choice_key]
    
	print(f"\nnum of {label.lower()} > ", end="", flush=True)

	value = input().strip()
	if not value.isdigit():
		return

	current = read_number(name)
	write_number(name, current + int(value))

def run():
	
	init_db()
	
	while True:
		
		clear_screen()
		view()
        
		choice = read_key().lower()
        
		if choice == "q":
			break
        
		try:
			choice_int = int(choice)
			if choice_int in EXERCISES:
				add_reps(choice_int)
		except ValueError:
			continue
