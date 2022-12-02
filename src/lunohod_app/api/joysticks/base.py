from __future__ import annotations

import typing as t
import abc
from threading import Thread
from dataclasses import dataclass
from datetime import datetime

if t.TYPE_CHECKING:
    from inputs import GamePad, InputEvent


class Joystick(Thread):
    def __init__(self, joystick: GamePad, events: list[ABCJoystickEvent]) -> None:
        super().__init__()

        self._joystick = joystick
        self._events = events

    def run(self):
        while True:
            self._read_joystick_events(self._joystick.read())

    def _prepare_joystick_event(self, joystick_event: InputEvent) -> JoystickInput:
        return JoystickInput(
            device=joystick_event.device,
            timestamp=datetime.fromtimestamp(joystick_event.timestamp),
            code=joystick_event.code,
            state=joystick_event.state,
        )

    def _read_joystick_events(self, joystick_events: list[InputEvent]) -> None:
        for joystick_event in joystick_events:
            if not(joystick_event.ev_type in ("Absolute", "Key")):
                continue

            for event in self._events:
                event.on_raw_event(self._prepare_joystick_event(joystick_event))


class ABCJoystickEvent(abc.ABC):
    def on_raw_event(self, event: JoystickInput) -> None:
        pass


@dataclass
class JoystickInput():
    device: GamePad
    timestamp: datetime
    code: str
    state: int
