from inputs import devices

from lunohod_app._app.joysticks import MyXBox360Joystick
from lunohod_app.api.joysticks import (
    Joystick,
)



try:
    joystick_device = devices.gamepads[0]
except IndexError:
    raise RuntimeError("Joystick no found.")


joystick = Joystick(joystick=joystick_device, events=[MyXBox360Joystick()])
joystick.start()
joystick.join()
