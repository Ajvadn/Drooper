# DROOPER - Social Engineering Tool
### Created by AJVAD-N

DROOPER is an advanced social engineering tool designed for penetration testing and security research. It helps security professionals generate and deliver payloads effectively through various attack vectors.

## 🚀 Features
✅ **Create malware payloads** (Reverse Shell with Metasploit)  
✅ **Start a Metasploit listener**  
✅ **Host a fake hacking course** for social engineering attacks  
✅ **Generate QR codes** for malware download links  
✅ **USB Auto-Copy** to spread malware via USB  
✅ **Ngrok Integration** for remote access  

---
## 📥 Installation
Ensure you have **Python 3**, **Metasploit**, and **Ngrok** installed.

### **Step 1: Clone the Repository**
```bash
git clone https://github.com/your-username/DROOPER.git
cd DROOPER
```

### **Step 2: Install Required Dependencies**
```bash
pip install -r requirements.txt
```

### **Step 3: Run the Tool**
```bash
python3 drooper.py
```

---
## 🛠 Usage Guide
Once launched, you’ll see the following menu:
```
1: Create Malware
2: Start Listener
3: Start Web Hosting Service
4: Generate Malware QR Code
5: Copy Malware to USB
6: Start Ngrok Tunnel
7: Exit
```

### **Create a Payload (Option 1)**
This generates `dropper.exe` in the `DROOPER_OUTPUT` folder.

### **Start Web Hosting (Option 3)**
- Hosts a fake **hacking course website** with a malware download link.
- Accessible via `http://localhost:8080`.

### **Start Ngrok Tunnel (Option 6)**
- Exposes the web server to the internet using Ngrok.
- Useful for **remote attacks**.

---
## ⚠️ Legal Disclaimer
🚨 **This tool is for educational and ethical testing purposes only.**  
Using it on **unauthorized systems is illegal** and punishable by law. The creator is **not responsible** for any misuse.

---
## 📢 Contributing
Want to improve DROOPER? Feel free to fork the repo and submit pull requests!

### **Contact:** AJVAD-N

🚀 Happy Ethical Hacking!

