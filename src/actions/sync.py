import sys
import time
import subprocess
from ui import clear_screen, read_key
import socket
import os

def fix_network():
    print("checking network...", end=" ", flush=True)
    try:
        socket.gethostbyname('github.com')
        print("OK")
    except socket.gaierror:
        print("DNS FAIL")
        print("patching /etc/resolv.conf...", end="")
        try:
            with open('/etc/resolv.conf', 'w') as f:
                f.write("nameserver 8.8.8.8\nnameserver 1.1.1.1\n")
            print("DONE")
        except PermissionError:
            print("FAILED (no root)")
    
    subprocess.run(["git", "fetch"])
    
def git_status():
    
    result = subprocess.run(
        ["git", "status"],
        text=True,
        capture_output=True
    )
    print(result.stdout)
    
    print("[q] [p]-push [d]-pull ", end="", flush=True)

def git_push():

    subprocess.run(["git", "add", "."])
    subprocess.run(["git", "commit", "-m", "upd"])
    subprocess.run(["git", "push"])
    
    print("\n[q] ", end="", flush=True)
    read_key()
    
def git_pull():
    
    subprocess.run(["git", "pull"])
    
    print("\n[q] ", end="", flush=True)
    read_key()

def run():
    
    fix_network()
    git_status()
    
    choice = read_key().lower()

    if choice == "p":

        clear_screen()
        git_push()
        
    elif choice == "d":
        
        clear_screen()
        git_pull()
