from gpiozero import Robot

class robot_handler():
    subjects = []
    robot_speed = 0.75

    def receive_message(self, event_type, message):
        if event_type == "MOVEMENT":
            print(event_type)
            if message == "BACKWARD":
                robot.backward(robot_speed)
            if message == "RIGHT":
                robot.right(robot_speed)
            if message == "LEFT":
                robot.left(robot_speed)
            if message == "FORWARD":
                robot.forward(robot_speed)
                print("FORWARD")
        elif event_type == "COMMAND":
            print(event_type)
            
