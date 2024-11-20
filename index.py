import shutil
import time

def monitor_drive(drive_letter):
    """Monitors the specified drive for file changes."""
    while True:
        try:
            # Path name to file to copy
            file_to_copy = "vm_microb.hex"
            destination = f"{drive_letter}:/vm_microb.hex"
            shutil.copyfile(file_to_copy, destination)
            print("Copied!")
            time.sleep(7)
        except FileNotFoundError:
            print(f"Drive {drive_letter} is not connected. Waiting...")
        time.sleep(1) 

# Monitor drive "D"
monitor_drive("D")