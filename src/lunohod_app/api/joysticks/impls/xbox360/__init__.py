from __future__ import annotations

import typing as t
import enum
from dataclasses import dataclass

from .events import XBox360JoystickEventsMixin, XBox360JoystickInput
from ...base import ABCJoystickEvent, JoystickInput


class XBox360Joystick(ABCJoystickEvent, XBox360JoystickEventsMixin):
    _MAX_TRIGGER_VALUE = 2 ** 8 - 1
    _MAX_STICK_VALUE = 2 ** 15 - 1

    def __init__(self) -> None:
        cjcmbn = self._create_joystick_code_methods_by_name
        self._CODES_TO_METHOD_DICT: dict[str, XBox360JoystickCodeMethods] = {
            "BTN_SOUTH": cjcmbn("south_button"),
            "BTN_NORTH": cjcmbn("north_button"),
            "BTN_WEST": cjcmbn("west_button"),
            "BTN_EAST": cjcmbn("east_button"),
            "BTN_SELECT": cjcmbn("select_button"),
            "BTN_START": cjcmbn("start_button"),
            "BTN_MODE": cjcmbn("mode_button"),
            "BTN_THUMBR": cjcmbn("right_stick_button"),
            "BTN_THUMBL": cjcmbn("left_stick_button"),
            "BTN_TR": cjcmbn("right_bumper_button"),
            "BTN_TL": cjcmbn("left_bumper_button"),
            "ABS_Y": cjcmbn("left_stick_y_absolute"),
            "ABS_X": cjcmbn("left_stick_x_absolute"),
            "ABS_RY": cjcmbn("right_stick_y_absolute"),
            "ABS_RX": cjcmbn("right_stick_x_absolute"),
            "ABS_HAT0X": cjcmbn("dpad_x_absolute"),
            "ABS_HAT0Y": cjcmbn("dpad_y_absolute"),
            "ABS_Z": cjcmbn("left_trigger_absolute"),
            "ABS_RZ": cjcmbn("right_trigger_absolute"),
        }

    def on_event(self, event: JoystickInput) -> None:
        try:
            methods = self._CODES_TO_METHOD_DICT[event.code]
        except KeyError:
            return

        self._call_event_methods(methods=methods, event=event)

    def _call_event_methods(
        self,
        methods: XBox360JoystickCodeMethods,
        event: JoystickInput,
    ) -> None:
        if event.code in ("ABS_Y", "ABS_X", "ABS_RY", "ABS_RX"):
            self._process_stick(methods=methods, event=event)
        elif event.code in ("ABS_Z", "ABS_RZ"):
            self._process_trigger(methods=methods, event=event)
        else:
            self._process_device(methods=methods, event=event)

    def _process_device(self, event: JoystickInput, methods: XBox360JoystickCodeMethods) -> None:
        state = event.state
        new_event = XBox360JoystickInput(
            state=state,
            device=event.device,
            code=event.code,
            timestamp=event.timestamp,
        )

        if event.state != 0:
            self._press(event=new_event, methods=methods)
        else:
            self._realize(event=new_event, methods=methods)

    def _process_trigger(self, event: JoystickInput, methods: XBox360JoystickCodeMethods) -> None:
        state = self._normalize_trigger_value(event.state)
        new_event = XBox360JoystickInput(
            state=state,
            device=event.device,
            code=event.code,
            timestamp=event.timestamp,
        )

        if event.state != 0:
            self._press(event=new_event, methods=methods)
        else:
            self._realize(event=new_event, methods=methods)

    def _process_stick(self, event: JoystickInput, methods: XBox360JoystickCodeMethods) -> None:
        state = self._normalize_stick_value(event.state)

        new_event = XBox360JoystickInput(
            state=state,
            device=event.device,
            code=event.code,
            timestamp=event.timestamp,
        )

        if (
            self._get_stick_coordinate(event.code) == StickCoordinate.Y
            and event.state == -1
        ):
            self._realize(event=new_event, methods=methods)
        elif event.state == 0:
            self._realize(event=new_event, methods=methods)
        else:
            self._press(event=new_event, methods=methods)

    def _get_stick_coordinate(self, code: str) -> StickCoordinate:
        return StickCoordinate.Y if code.endswith("Y") else StickCoordinate.X

    def _realize(self, event: XBox360JoystickInput, methods: XBox360JoystickCodeMethods) -> None:
        self.on_realized(event)
        methods.realized(event)

    def _press(self, event: XBox360JoystickInput, methods: XBox360JoystickCodeMethods) -> None:
        self.on_pressed(event)
        methods.pressed(event)

    def _normalize_stick_value(self, state: int) -> float:
        return state / self._MAX_STICK_VALUE

    def _normalize_trigger_value(self, state: int) -> float:
        return state / self._MAX_TRIGGER_VALUE

    def _create_joystick_code_methods_by_name(self, name: str) -> "XBox360JoystickCodeMethods":
        prefix = f"on_{name}"
        return XBox360JoystickCodeMethods(
            pressed=getattr(self, f"{prefix}_pressed"),
            realized=getattr(self, f"{prefix}_realized"),
        )

@dataclass
class XBox360JoystickCodeMethods():
    pressed: t.Callable[[XBox360JoystickInput], None]
    realized: t.Callable[[XBox360JoystickInput], None]


class StickCoordinate(enum.Enum):
    X = enum.auto()
    Y = enum.auto
