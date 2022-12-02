# TODO: New level of abstract
from __future__ import annotations

import typing as t

from .joystick import XBox360Joystick

if t.TYPE_CHECKING:
    from ...base import JoystickInput


class PressControllerXBox360Joystick(XBox360Joystick):
    def __init__(self) -> None:
        super().__init__()

        self._pressed_keys = set[str]()

    def on_pressed(self, event: JoystickInput) -> None:
        self._pressed_keys.add(event.code)

    def on_realized(self, event: JoystickInput) -> None:
        self._pressed_keys.remove(event.code)
