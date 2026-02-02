from actions import git
from ui import clear_last_line
import time


def update():
	print("fetch ",end="", flush=True)
    
	try:
		git.git_fetch()
        
		if git.has_remote_commits():
			clear_last_line()
			print("pull ",end="", flush=True)
			git.git_pull()
            
	except Exception:
		pass
    
	clear_last_line()
