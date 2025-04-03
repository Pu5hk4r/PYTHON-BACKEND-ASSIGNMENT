import subprocess
import time
import os

def start_emulator(avd_name):
    try:
        process = subprocess.Popen(['emulator', '-avd', avd_name])
        # Wait for boot completion
        while True:
            output = subprocess.check_output(['adb', 'shell', 'getprop', 'sys.boot_completed']).decode().strip()
            if output == '1':
                break
            time.sleep(5)  # Check every 5 seconds
    except subprocess.CalledProcessError as e:
        print(f"Error starting emulator: {e}")
        raise

def get_emulator_id():
    try:
        output = subprocess.check_output(['adb', 'devices']).decode()
        lines = output.strip().split('\n')[1:]  # Skip header
        for line in lines:
            if 'emulator' in line and 'device' in line:
                return line.split()[0]  # Returns serial like "emulator-5554"
        raise ValueError("No emulator found")
    except subprocess.CalledProcessError as e:
        print(f"Error getting device list: {e}")
        raise

def install_apk(apk_path, device_id):
    try:
        if not os.path.exists(apk_path):
            raise FileNotFoundError(f"APK file not found: {apk_path}")
        subprocess.run(['adb', '-s', device_id, 'install', apk_path], check=True)
    except FileNotFoundError as e:
        print(f"Error: {e}")
        raise
    except subprocess.CalledProcessError as e:
        print(f"Error installing APK: {e}")
        raise
    except Exception as e:
        print(f"Unexpected error: {e}")
        raise

def get_system_info(device_id):
    try:
        os_version = subprocess.check_output(['adb', '-s', device_id, 'shell', 'getprop', 'ro.build.version.release']).decode().strip()
        ram_info = subprocess.check_output(['adb', '-s', device_id, 'shell', 'cat', '/proc/meminfo']).decode().split('\n')[0]
        return {'os_version': os_version, 'ram': ram_info}
    except subprocess.CalledProcessError as e:
        print(f"Error getting system info: {e}")
        raise

if __name__ == '__main__':
    avd_name = 'Medium_Phone_API_36'

    apk_path = 'app.apk'
    start_emulator(avd_name)
    device_id = get_emulator_id()
    install_apk(apk_path, device_id)
    system_info = get_system_info(device_id)
    with open('system_info.txt', 'w') as f:
        f.write(f"OS Version: {system_info['os_version']}\n")
        f.write(f"RAM Info: {system_info['ram']}\n")
    print(system_info)