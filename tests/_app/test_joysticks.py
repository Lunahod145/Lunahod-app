from inputs import devices

from lunohod_app._app.joystick.concrete_xbox360_joystick import ConcreteXBox360Joystick
from lunohod_app.api.joysticks import Joystick


class CustomConcreteXBox360Joystick(ConcreteXBox360Joystick):
    def on_pressed(self, event) -> None:
        super().on_pressed(event)
        print(self._pressed_keys)


try:
    joystick_device = devices.gamepads[0]
except IndexError:
    raise RuntimeError("Joystick no found.")


joystick = Joystick(joystick=joystick_device, events=[CustomConcreteXBox360Joystick()])
joystick.start()
joystick.join()
