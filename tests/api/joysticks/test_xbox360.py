from inputs import devices

from lunohod_app.api.joysticks import (
    XBox360Joystick,
    Joystick,
)


class CustomXBox360Joystick(XBox360Joystick):
    def on_pressed(self, event) -> None:
       print("Press:", event.code, event.state)

    def on_realized(self, event) -> None:
       print("Realize:", event.code, event.state)


try:
    joystick_device = devices.gamepads[0]
except IndexError:
    raise RuntimeError("Joystick no found.")


joystick = Joystick(joystick=joystick_device, events=[CustomXBox360Joystick()])
joystick.start()
joystick.join()
