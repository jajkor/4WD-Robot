
class controller_input:    
    def __init__(self, gamepad):
        self.gamepad = gamepad
        self.component = []

    def append_component(self, com):
        component.append(com)
    
    def handle_input():
        for event in gamepad.read_loop():
            if event.type == ecodes.EV_KEY:
                if event.value == 1:
                    if event.code == key_mappings["BTN_B"]:
                        send_message("MOVEMENT", "BACKWARD")
                        print('BACKWARD')
                    if event.code == key_mappings["BTN_A"]:
                        send_message("MOVEMENT", "RIGHT")
                        print('RIGHT')    
                    if event.code == key_mappings["BTN_Y"]:
                        send_message("MOVEMENT", "LEFT")
                        print('LEFT')
                    if event.code == key_mappings["BTN_X"]:
                        send_message("MOVEMENT", "FORWARD")
                        print('FORWARD')

    def send_message(self, event_type, message):
        for component in components:
            component.receive_message(event_type, message)
