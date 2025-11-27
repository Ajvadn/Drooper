from pyngrok import conf, ngrok
import os

print(f"Ngrok path from config: {conf.get_default().ngrok_path}")

# Try to install if not present
if not os.path.exists(conf.get_default().ngrok_path):
    print("Ngrok binary not found. Installing...")
    try:
        ngrok.install_ngrok()
        print(f"Installed to: {conf.get_default().ngrok_path}")
    except Exception as e:
        print(f"Failed to install: {e}")
else:
    print("Ngrok binary exists.")
