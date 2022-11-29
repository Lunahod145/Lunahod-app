import typing as t
from dataclasses import dataclass

from .events import XBox360JoystickEventsMixin
from ...base import ABCJoystickEvent, JoystickInput


class XBox360Joystick(ABCJoystickEvent, XBox360JoystickEventsMixin):
    _MAX_TRIGGER_VALUE = 2 ** 8
    _MAX_JOYSTICK_VALUE = 2 ** 15

    def __init__(self) -> None:
        cjcmbn = self._create_joystick_code_methods_by_name
        self._CODES_TO_METHOD_DICT: dict[str, "XBox360JoystickCodeMethods"] = {
            "BTN_SOUTH": cjcmbn("south_button"),
            "BTN_NORTH": cjcmbn("north_button"),
            "BTN_WEST": cjcmbn("west_button"),
            "BTN_EAST": cjcmbn("east_button"),
            "BTN_SELECT": cjcmbn("select_button"),
            "BTN_START": cjcmbn("start_button"),
            "BTN_MODE": cjcmbn("mode_button"),
            "BTN_THUMBR": cjcmbn("right_joystick_button"),
            "BTN_THUMBL": cjcmbn("left_joystick_button"),
            "BTN_TR": cjcmbn("right_bumper_button"),
            "BTN_TL": cjcmbn("left_bumper_button"),
            "ABS_Y": cjcmbn("left_joystick_y_absolute"),
            "ABS_X": cjcmbn("left_joystick_x_absolute"),
            "ABS_RY": cjcmbn("right_joystick_y_absolute"),
            "ABS_RX": cjcmbn("right_joystick_x_absolute"),
            "ABS_HAT0X": cjcmbn("dpad_x_absolute"),
            "ABS_HAT0Y": cjcmbn("dpad_y_absolute"),
        }

    def on_event(self, event: JoystickInput) -> None:
        try:
            methods = self._CODES_TO_METHOD_DICT[event.code]
        except KeyError:
            return

        self._call_desired_method(methods=methods, event=event)

    def _call_desired_method(
        self,
        methods: "XBox360JoystickCodeMethods",
        event: JoystickInput,
    ) -> None:

        state = self._normalize_state(event=event)

        if state == 0:
            methods.realized(event)
        else:
            methods.pressed(event)

    def _normalize_state(self, event: JoystickInput) -> float:
        if event.code in ("ABS_Y", "ABS_X", "ABS_RY", "ABS_RX"):
            return self._normalize_trigger_value(event.state)
        elif event.code in ("ABS_Z", "ABS_RZ"):
            return self._normalize_joystick_value(event.state)
        else:
            return event.state

    def _normalize_trigger_value(self, state: int) -> float:
        return state / self._MAX_TRIGGER_VALUE

    def _normalize_joystick_value(self, state: int) -> float:
        return state / self._MAX_TRIGGER_VALUE

    def _create_joystick_code_methods_by_name(self, name: str) -> "XBox360JoystickCodeMethods":
        prefix = f"on_{name}"
        return XBox360JoystickCodeMethods(
            pressed=getattr(self, f"{prefix}_pressed"),
            realized=getattr(self, f"{prefix}_realized"),
        )

@dataclass
class XBox360JoystickCodeMethods():
    pressed: t.Callable[[JoystickInput], None]
    realized: t.Callable[[JoystickInput], None]
