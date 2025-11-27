# DROOPER - Advanced Social Engineering Tool
### Created by AJVAD-N

DROOPER is a powerful social engineering tool designed for penetration testing and security research. It streamlines the process of generating payloads, hosting fake websites, and delivering attacks.

## 🚀 New Features (v2.0)
*   **Modern CLI**: A beautiful, interactive command-line interface using `rich` and `pyfiglet`.
*   **Professional Web Interface**: A legitimate-looking "SecureLearning" e-learning platform to host your payloads, designed to fool targets.
*   **Universal Terminal Support**: Automatically detects your environment (Tmux, Gnome, Konsole, Xfce, Xterm) and opens listeners/tunnels in new tabs or split panes.
*   **Smart Ngrok Integration**: Automatically finds your Ngrok installation and handles authentication.
*   **Easy Run Script**: Simple `./run.sh` script handles virtual environments and dependencies for you.

## ✨ Capabilities
✅ **Create Malware Payloads** (Reverse Shell with Metasploit)  
✅ **Start Metasploit Listener** (Auto-configured with `resource` scripts)  
✅ **Host Fake E-Learning Website** (Professional "SecureLearning" template)  
✅ **Generate QR Codes** for malware download links  
✅ **USB Auto-Copy** to spread malware via USB  
✅ **Ngrok Integration** for remote access  

---

## 📥 Installation

### **Step 1: Clone the Repository**
```bash
git clone https://github.com/Ajvadn/Drooper.git
cd Drooper
```

### **Step 2: Run the Tool**
We have provided a helper script that sets up the virtual environment and installs dependencies automatically.
```bash
chmod +x run.sh
./run.sh
```

Alternatively, you can run it manually:
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 main.py
```

---

## 🛠 Usage Guide

### **1. Create Malware Payload**
Generates a `dropper.exe` payload using `msfvenom`. You can specify a custom LHOST or use the detected local IP.

### **2. Start Metasploit Listener**
Starts `msfconsole` with a pre-configured listener.
*   **Split Terminal**: If running in `tmux`, it splits the pane.
*   **New Tab**: If in a desktop environment, it opens a new terminal tab.

### **3. Start Web Hosting Service**
Hosts the **"SecureLearning"** fake course website on port 8080.
*   The payload is hidden behind the "Download Course Materials" button.
*   **URL**: `http://localhost:8080`

### **4. Generate Malware QR Code**
Generates a QR code pointing to your hosted payload. Great for mobile-targeted attacks.

### **5. Copy Malware to USB**
Automatically detects connected USB drives and copies the payload to them as `usb_drop.exe`.

### **6. Start Ngrok Tunnel**
Exposes your local web server to the internet.
*   **Auto-Auth**: Prompts to configure your Ngrok authtoken if missing.
*   **New Tab/Split**: Opens Ngrok status in a separate view.

---

## ⚠️ Legal Disclaimer
🚨 **This tool is for educational and ethical testing purposes only.**  
Using it on **unauthorized systems is illegal** and punishable by law. The creator is **not responsible** for any misuse. Always obtain permission before testing.

---

## 📢 Contributing
Want to improve DROOPER? Feel free to fork the repo and submit pull requests!

### **Contact:** AJVAD-N

🚀 Happy Ethical Hacking!
