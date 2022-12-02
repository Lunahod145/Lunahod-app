from __future__ import annotations

import typing as t

if t.TYPE_CHECKING:
    from .devices import XBox360JoystickInput


class XBox360JoystickEventsMixin():
    def on_pressed(self, event: XBox360JoystickInput) -> None: pass
    def on_realized(self, event: XBox360JoystickInput) -> None: pass

    def on_south_button_pressed(self, event: XBox360JoystickInput) -> None: pass
    def on_east_button_pressed(self, event: XBox360JoystickInput) -> None: pass
    def on_west_button_pressed(self, event: XBox360JoystickInput) -> None: pass
    def on_north_button_pressed(self, event: XBox360JoystickInput) -> None: pass
    def on_select_button_pressed(self, event: XBox360JoystickInput) -> None: pass
    def on_start_button_pressed(self, event: XBox360JoystickInput) -> None: pass
    def on_mode_button_pressed(self, event: XBox360JoystickInput) -> None: pass
    def on_left_stick_button_pressed(self, event: XBox360JoystickInput) -> None: pass
    def on_right_stick_button_pressed(self, event: XBox360JoystickInput) -> None: pass
    def on_left_bumper_button_pressed(self, event: XBox360JoystickInput) -> None: pass
    def on_right_bumper_button_pressed(self, event: XBox360JoystickInput) -> None: pass

    def on_left_stick_y_absolute_pressed(self, event: XBox360JoystickInput) -> None: pass
    def on_left_stick_x_absolute_pressed(self, event: XBox360JoystickInput) -> None: pass
    def on_right_stick_y_absolute_pressed(self, event: XBox360JoystickInput) -> None: pass
    def on_right_stick_x_absolute_pressed(self, event: XBox360JoystickInput) -> None: pass
    def on_dpad_x_absolute_pressed(self, event: XBox360JoystickInput) -> None: pass
    def on_dpad_y_absolute_pressed(self, event: XBox360JoystickInput) -> None: pass
    def on_left_trigger_absolute_pressed(self, event: XBox360JoystickInput) -> None: pass
    def on_right_trigger_absolute_pressed(self, event: XBox360JoystickInput) -> None: pass

    def on_south_button_realized(self, event: XBox360JoystickInput) -> None: pass
    def on_east_button_realized(self, event: XBox360JoystickInput) -> None: pass
    def on_west_button_realized(self, event: XBox360JoystickInput) -> None: pass
    def on_north_button_realized(self, event: XBox360JoystickInput) -> None: pass
    def on_select_button_realized(self, event: XBox360JoystickInput) -> None: pass
    def on_start_button_realized(self, event: XBox360JoystickInput) -> None: pass
    def on_mode_button_realized(self, event: XBox360JoystickInput) -> None: pass
    def on_left_stick_button_realized(self, event: XBox360JoystickInput) -> None: pass
    def on_right_stick_button_realized(self, event: XBox360JoystickInput) -> None: pass
    def on_left_bumper_button_realized(self, event: XBox360JoystickInput) -> None: pass
    def on_right_bumper_button_realized(self, event: XBox360JoystickInput) -> None: pass

    def on_left_stick_y_absolute_realized(self, event: XBox360JoystickInput) -> None: pass
    def on_left_stick_x_absolute_realized(self, event: XBox360JoystickInput) -> None: pass
    def on_right_stick_y_absolute_realized(self, event: XBox360JoystickInput) -> None: pass
    def on_right_stick_x_absolute_realized(self, event: XBox360JoystickInput) -> None: pass
    def on_dpad_x_absolute_realized(self, event: XBox360JoystickInput) -> None: pass
    def on_dpad_y_absolute_realized(self, event: XBox360JoystickInput) -> None: pass
    def on_left_trigger_absolute_realized(self, event: XBox360JoystickInput) -> None: pass
    def on_right_trigger_absolute_realized(self, event: XBox360JoystickInput) -> None: pass
