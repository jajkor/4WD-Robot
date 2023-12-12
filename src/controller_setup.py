import json
from evdev import InputDevice, ecodes
import evdev

def load_controller():
    try:
        devices = [evdev.InputDevice(path) for path in evdev.list_devices()]
        for device in devices:
            if device.name == 'Pro Controller':
                file_path = device.path
                gamepad = InputDevice(file_path)
                return gamepad
    except:
        print('Controller not found.')

def load_controller_config(config_path):   
    try:
        with open(config_path, "r") as jsonfile:
            data = json.load(jsonfile)
            controller_config = dict(data)
            jsonfile.close()
            return controller_config
    except:
        print('Input Configuration file not found.')
