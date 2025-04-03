import subprocess
import requests
import time

def get_device_id():
    """Get first connected emulator ID using adb"""
    try:
        output = subprocess.check_output(['adb', 'devices'], text=True)
        devices = [line.split('\t')[0] for line in output.split('\n')[1:] if 'emulator' in line]
        return devices[0] if devices else None
    except subprocess.CalledProcessError as e:
        print(f"ADB Error: {e}")
        return None

def get_system_info(device_id):
    """Get Android system info using adb commands"""
    try:
        os_version = subprocess.check_output(
            ['adb', '-s', device_id, 'shell', 'getprop', 'ro.build.version.release'],
            text=True
        ).strip()
        
        model = subprocess.check_output(
            ['adb', '-s', device_id, 'shell', 'getprop', 'ro.product.model'],
            text=True
        ).strip()

        return {
            'device_id': device_id,
            'os_version': os_version,
            'model': model
        }
    except subprocess.CalledProcessError as e:
        print(f"Failed to get system info: {e}")
        return None

def send_to_backend(data):
    """Send data to Flask API"""
    try:
        response = requests.post(
            'http://localhost:5000/receive-data',
            json=data,
            timeout=10
        )
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"API Error: {e}")
        return None

if __name__ == '__main__':
    # Wait for emulator to fully boot
    time.sleep(15)
    
    if (device_id := get_device_id()):
        system_info = get_system_info(device_id)
        if system_info:
            print("Sending data:", system_info)
            response = send_to_backend(system_info)
            print("Server response:", response)
        else:
            print("Failed to collect system info")
    else:
        print("No emulator found. Start the emulator first.")