from gpiozero import Robot, DistanceSensor
from evdev import InputDevice, ecodes
import evdev
from myrobot.input_config import new_input_config

config_path = "myrobot/config.json"

sensor = DistanceSensor(echo=9, trigger=10, max_distance=1, threshold_distance=0.2)
robot = Robot(left=(23, 24, 25), right=(17, 27, 22))

key_mappings = {
    "BTN_A": 305,
    "BTN_B": 304,
    "BTN_X": 307,
    "BTN_Y": 306,
    "BTN_MODE": 316,
    "BTN_CAMERA": 317,
    "BTN_MINUS": 312,
    "BTN_PLUS": 313,   
}

ic = new_input_config(config_path)
print(ic["BTN_A"])

try:
    devices = [evdev.InputDevice(path) for path in evdev.list_devices()]
    for device in devices:
        if device.name == 'Pro Controller':
            file_path = device.path
            
    gamepad = InputDevice(file_path)
    print(gamepad)

    robotSpeed = 0.75

    enableSafetyMode = True

    sensor.when_in_range = robot.stop

    for event in gamepad.read_loop():
        if event.type == ecodes.EV_KEY:
            if event.value == 1:
                if event.code == key_mappings["BTN_B"]:
                    robot.backward(robotSpeed)
                    print('BACKWARD')
                if event.code == key_mappings["BTN_A"]:
                    robot.right(robotSpeed)
                    print('RIGHT')    
                if event.code == key_mappings["BTN_Y"]:
                    robot.left(robotSpeed)
                    print('LEFT')
                if event.code == key_mappings["BTN_X"]:
                    robot.forward(robotSpeed)
                    print('FORWARD')
                if event.code == key_mappings["BTN_MINUS"] and not robot.is_active:
                    if robotSpeed <= 1 and robotSpeed > 0.25:
                        robotSpeed -= 0.25
                    print(robotSpeed)    
                if event.code == key_mappings["BTN_PLUS"] and not robot.is_active:
                    if robotSpeed < 1 and robotSpeed >= 0:
                        robotSpeed += 0.25
                    print(robotSpeed)
                if event.code == key_mappings["BTN_CAMERA"] and not robot.is_active:
                    if enableSafetyMode:
                        enableSafetyMode = False
                    else:
                        enableSafetyMode = True
                    print(enableSafetyMode)
                    print('SAFETY MODE')
                if event.code == key_mappings["BTN_MODE"]:
                    robot.stop()
                    print('HOME')  
except:
    print('Pro Controller not found, make sure it is connected to Bluetooth\nconnect 74:F9:CA:51:02:14')    
