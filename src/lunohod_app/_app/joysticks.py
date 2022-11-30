import code
from lunohod_app.api.joysticks import XBox360Joystick, JoystickInput


class MyXBox360Joystick(XBox360Joystick):
    def __init__(self) -> None:
        super().__init__()

        self._pressed_keys = []

    def on_pressed(self, event: JoystickInput) -> None:
        self._pressed_keys.append(event.code)

    def on_realized(self, event: JoystickInput) -> None:
        self._pressed_keys.remove(event.code)
