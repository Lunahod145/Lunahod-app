from lunohod_app.api.joysticks import JoystickEvent, JoystickInput


class AButtonEvent(JoystickEvent):
    def do(self, event: JoystickInput) -> None:
        if event.state == 1:
            print(1)
