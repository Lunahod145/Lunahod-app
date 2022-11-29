from inputs import devices

from lunohod_app.api.joysticks.base import Joystick
from lunohod_app.api.joysticks.impls.xbox360 import XBox360Joystick, JoystickInput


class CustomXBox360Joystick(XBox360Joystick):
    def on_south_button_pressed(self, event: JoystickInput) -> None:
        self._processing_event(event)

    def on_east_button_pressed(self, event: JoystickInput) -> None:
        self._processing_event(event)

    def on_west_button_pressed(self, event: JoystickInput) -> None:
        self._processing_event(event)

    def on_north_button_pressed(self, event: JoystickInput) -> None:
        self._processing_event(event)

    def on_select_button_pressed(self, event: JoystickInput) -> None:
        self._processing_event(event)

    def on_start_button_pressed(self, event: JoystickInput) -> None:
        self._processing_event(event)

    def on_mode_button_pressed(self, event: JoystickInput) -> None:
        self._processing_event(event)

    def on_left_joystick_button_pressed(self, event: JoystickInput) -> None:
        self._processing_event(event)

    def on_right_joystick_button_pressed(self, event: JoystickInput) -> None:
        self._processing_event(event)

    def on_left_bumper_button_pressed(self, event: JoystickInput) -> None:
        self._processing_event(event)

    def on_right_bumper_button_pressed(self, event: JoystickInput) -> None:
        self._processing_event(event)

    def on_left_joystick_y_absolute_pressed(self, event: JoystickInput) -> None:
        self._processing_event(event)

    def on_left_joystick_x_absolute_pressed(self, event: JoystickInput) -> None:
        self._processing_event(event)

    def on_right_joystick_y_absolute_pressed(self, event: JoystickInput) -> None:
        self._processing_event(event)

    def on_right_joystick_x_absolute_pressed(self, event: JoystickInput) -> None:
        self._processing_event(event)

    def on_dpad_x_absolute_pressed(self, event: JoystickInput) -> None:
        self._processing_event(event)

    def on_dpad_y_absolute_pressed(self, event: JoystickInput) -> None:
        self._processing_event(event)

    def on_south_button_realized(self, event: JoystickInput) -> None:
        self._processing_event(event)

    def on_east_button_realized(self, event: JoystickInput) -> None:
        self._processing_event(event)

    def on_west_button_realized(self, event: JoystickInput) -> None:
        self._processing_event(event)

    def on_north_button_realized(self, event: JoystickInput) -> None:
        self._processing_event(event)

    def on_select_button_realized(self, event: JoystickInput) -> None:
        self._processing_event(event)

    def on_start_button_realized(self, event: JoystickInput) -> None:
        self._processing_event(event)

    def on_mode_button_realized(self, event: JoystickInput) -> None:
        self._processing_event(event)

    def on_left_joystick_button_realized(self, event: JoystickInput) -> None:
        self._processing_event(event)

    def on_right_joystick_button_realized(self, event: JoystickInput) -> None:
        self._processing_event(event)

    def on_left_bumper_button_realized(self, event: JoystickInput) -> None:
        self._processing_event(event)

    def on_right_bumper_button_realized(self, event: JoystickInput) -> None:
        self._processing_event(event)

    def on_left_joystick_y_absolute_realized(self, event: JoystickInput) -> None:
        self._processing_event(event)

    def on_left_joystick_x_absolute_realized(self, event: JoystickInput) -> None:
        self._processing_event(event)

    def on_right_joystick_y_absolute_realized(self, event: JoystickInput) -> None:
        self._processing_event(event)

    def on_right_joystick_x_absolute_realized(self, event: JoystickInput) -> None:
        self._processing_event(event)

    def on_dpad_x_absolute_realized(self, event: JoystickInput) -> None:
        self._processing_event(event)

    def on_dpad_y_absolute_realized(self, event: JoystickInput) -> None:
        self._processing_event(event)

    def _processing_event(self, event: JoystickInput) -> None:
        print(event)


try:
    joystick_device = devices.gamepads[0]
except IndexError:
    raise RuntimeError("Joystick no found.")


joystick = Joystick(joystick=joystick_device, events=[CustomXBox360Joystick()])
joystick.start()
joystick.join()
