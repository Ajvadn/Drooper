import socket
import os
import shutil
import subprocess

def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        local_ip = s.getsockname()[0]
        s.close()
        return local_ip
    except Exception:
        return "127.0.0.1"

def setup_output_directory():
    output_dir = "DROOPER_OUTPUT"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    return output_dir

def spawn_terminal(cmd):
    """
    Spawns a command in a new terminal window or split pane.
    Supports: Tmux, Gnome Terminal, Konsole, Xfce4 Terminal, Xterm.
    """
    # 1. Check for Tmux
    if os.environ.get('TMUX'):
        os.system(f"tmux split-window -h \"{cmd}\"")
        return True

    # 2. Check for common terminal emulators
    if shutil.which("gnome-terminal"):
        os.system(f"gnome-terminal --tab -- bash -c '{cmd}; exec bash'")
        return True
    
    if shutil.which("konsole"):
        os.system(f"konsole --new-tab -e bash -c '{cmd}; exec bash'")
        return True

    if shutil.which("xfce4-terminal"):
        os.system(f"xfce4-terminal --tab -e \"bash -c '{cmd}; exec bash'\"")
        return True

    if shutil.which("xterm"):
        os.system(f"xterm -e \"{cmd}; exec bash\" &")
        return True
        
    return False
