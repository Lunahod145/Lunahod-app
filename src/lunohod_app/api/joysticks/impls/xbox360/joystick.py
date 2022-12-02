from __future__ import annotations

import typing as t
from dataclasses import dataclass
from logging import getLogger

from .events_mixin import XBox360JoystickEventsMixin
from .devices import (
    ABC_XBox360Device,
    CommonXBox360Device,
    TriggerXBox360Device,
    StickXBox360Device,
    XBox360ProcessResultType,
    XBox360JoystickInput,
)
from ...base import ABCJoystickEvent

if t.TYPE_CHECKING:
    from ...base import JoystickInput


_log = getLogger(__name__)


class XBox360Joystick(ABCJoystickEvent, XBox360JoystickEventsMixin):
    def __init__(self) -> None:
        cm = XBox360JoystickCodeMethods
        self._CODES_TO_METHOD_DICT: dict[str, XBox360JoystickCodeMethods] = {
            "BTN_SOUTH": cm(self.on_south_button_pressed, self.on_south_button_realized),
            "BTN_NORTH": cm(self.on_north_button_pressed, self.on_north_button_realized),
            "BTN_WEST": cm(self.on_west_button_pressed, self.on_west_button_realized),
            "BTN_EAST": cm(self.on_east_button_pressed, self.on_east_button_realized),
            "BTN_SELECT": cm(self.on_select_button_pressed, self.on_select_button_realized),
            "BTN_START": cm(self.on_start_button_pressed, self.on_start_button_realized),
            "BTN_MODE": cm(self.on_mode_button_pressed, self.on_mode_button_realized),
            "BTN_THUMBR": cm(self.on_right_stick_button_pressed, self.on_right_stick_button_realized),
            "BTN_THUMBL": cm(self.on_left_stick_button_pressed, self.on_left_stick_button_realized),
            "BTN_TR": cm(self.on_right_bumper_button_pressed, self.on_right_bumper_button_realized),
            "BTN_TL": cm(self.on_left_bumper_button_pressed, self.on_left_bumper_button_realized),
            "ABS_Y": cm(self.on_left_stick_y_absolute_pressed, self.on_left_stick_y_absolute_realized),
            "ABS_X": cm(self.on_left_stick_x_absolute_pressed, self.on_left_stick_x_absolute_realized),
            "ABS_RY": cm(self.on_right_stick_y_absolute_pressed, self.on_right_stick_y_absolute_realized),
            "ABS_RX": cm(self.on_right_stick_x_absolute_pressed, self.on_right_stick_x_absolute_realized),
            "ABS_HAT0X": cm(self.on_dpad_x_absolute_pressed, self.on_dpad_x_absolute_realized),
            "ABS_HAT0Y": cm(self.on_dpad_y_absolute_pressed, self.on_dpad_y_absolute_realized),
            "ABS_Z": cm(self.on_left_trigger_absolute_pressed, self.on_left_trigger_absolute_realized),
            "ABS_RZ": cm(self.on_right_trigger_absolute_pressed, self.on_right_trigger_absolute_realized),
        }

    def on_raw_event(self, event: JoystickInput) -> None:
        try:
            methods = self._CODES_TO_METHOD_DICT[event.code]
        except KeyError as error:
            _log.warning(f"Event {error.args[0]} is not supported")
            return

        self._call_event_methods(methods=methods, event=event)

    def _call_event_methods(
        self,
        event: JoystickInput,
        methods: XBox360JoystickCodeMethods,
    ) -> None:
        device = self._get_device_by_event(event)
        result = device.process(event)

        if result.type == XBox360ProcessResultType.PRESS:
            self._press(event=result.event, methods=methods)
        else:
            self._realize(event=result.event, methods=methods)

    def _get_device_by_event(self, event: JoystickInput) -> ABC_XBox360Device:
        if event.code in ("ABS_Y", "ABS_X", "ABS_RY", "ABS_RX"):
            return StickXBox360Device()
        elif event.code in ("ABS_Z", "ABS_RZ"):
            return TriggerXBox360Device()
        else:
            return CommonXBox360Device()

    def _realize(self, event: XBox360JoystickInput, methods: XBox360JoystickCodeMethods) -> None:
        self.on_realized(event)
        methods.realized(event)

    def _press(self, event: XBox360JoystickInput, methods: XBox360JoystickCodeMethods) -> None:
        self.on_pressed(event)
        methods.pressed(event)


@dataclass
class XBox360JoystickCodeMethods():
    pressed: t.Callable[[XBox360JoystickInput], None]
    realized: t.Callable[[XBox360JoystickInput], None]
