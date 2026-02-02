from actions import git
from ui import clear_last_line
import time


def update():
	print(".. ",end="", flush=True)
    
	try:
		git.git_fetch()
        
		if git.has_remote_commits():
			git.git_pull()
            
	except Exception:
		pass
    
	clear_last_line()
