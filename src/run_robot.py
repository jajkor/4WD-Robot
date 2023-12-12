from gpiozero import Robot, DistanceSensor
from evdev import ecodes
from controller_setup import load_controller, load_controller_config

config_path = "pro-config.json"

def main():
    # Setup Bluetooth Controller
    gamepad = load_controller()
    print(gamepad)
    controller_config = load_controller_config(config_path)
    print(controller_config)
    # Setup Robot
    robot = Robot(left=(23, 24, 25), right=(16, 20, 21))
    robotSpeed = 0.75
    # Setup Sensor
    sensor = DistanceSensor(echo=17, trigger=3, max_distance=1, threshold_distance=0.2)

    sensor.when_in_range = robot.stop

    for event in gamepad.read_loop():
        if event.type == ecodes.EV_KEY:
            if event.value == 1:
                if event.code == controller_config["BTN_B"]:
                    robot.backward(robotSpeed)
                    print('BACKWARD')
                if event.code == controller_config["BTN_A"]:
                    robot.left_motor.backward(robotSpeed/2)
                    robot.right_motor.forward(robotSpeed)
                    print('RIGHT')    
                if event.code == controller_config["BTN_Y"]:
                    robot.left_motor.forward(robotSpeed)
                    robot.right_motor.backward(robotSpeed/2)
                    print('LEFT')
                if event.code == controller_config["BTN_X"]:
                    robot.forward(robotSpeed)
                    print('FORWARD')
                if event.code == controller_config["BTN_MINUS"] and not robot.is_active:
                    if robotSpeed <= 1 and robotSpeed > 0.25:
                        robotSpeed -= 0.25
                    print(robotSpeed)    
                if event.code == controller_config["BTN_PLUS"] and not robot.is_active:
                    if robotSpeed < 1 and robotSpeed >= 0:
                        robotSpeed += 0.25
                    print(robotSpeed)
                if event.code == controller_config["BTN_CAMERA"] and not robot.is_active:
                    if enableSafetyMode:
                        enableSafetyMode = False
                    else:
                        enableSafetyMode = True
                    print(enableSafetyMode)
                    print('SAFETY MODE')
                if event.code == controller_config["BTN_MODE"]:
                    robot.stop()
                    print('HOME')  

if __name__ == '__main__':
    main()
