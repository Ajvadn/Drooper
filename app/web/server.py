import os
import threading
import time
from flask import Flask, render_template, send_from_directory
from app.core.utils import setup_output_directory, spawn_terminal

app = Flask(__name__)

# Disable Flask banner
import logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download/<filename>')
def download_file(filename):
    return send_from_directory(os.path.abspath(setup_output_directory()), filename)

import socket

def is_port_in_use(port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        return s.connect_ex(('localhost', port)) == 0

def run_flask():
    try:
        app.run(host='0.0.0.0', port=8080)
    except OSError as e:
        if e.errno == 98: # Address already in use
            print("[!] Port 8080 is already in use. Server might be running already.")
        else:
            raise e

def start_web_server():
    if is_port_in_use(8080):
        print("[!] Port 8080 is busy. Assuming server is already running.")
        return None
        
    flask_thread = threading.Thread(target=run_flask, daemon=True)
    flask_thread.start()
    return flask_thread

def start_ngrok_tunnel(new_tab=False):
    # Ensure Flask is running
    flask_thread = start_web_server()
    time.sleep(2) # Give it a moment
    
    from pyngrok import conf, ngrok
    
    # Ensure ngrok is installed
    if not os.path.exists(conf.get_default().ngrok_path):
        try:
            ngrok.install_ngrok()
        except Exception as e:
            print(f"[!] Failed to install ngrok: {e}")
            return

    ngrok_path = conf.get_default().ngrok_path
    
    # Find config file
    config_path = os.path.join(os.path.expanduser("~"), ".config", "ngrok", "ngrok.yml")
    if not os.path.exists(config_path):
        # Fallback to default if not found, though we know it exists
        cmd = f"{ngrok_path} http 8080"
    else:
        cmd = f"{ngrok_path} http 8080 --config {config_path}"
    
    if new_tab:
        if spawn_terminal(cmd):
            return
        else:
            print("[!] No supported terminal emulator found. Running in background.")
            os.system(f"{cmd} &")
    else:
        os.system(f"{cmd} &")
