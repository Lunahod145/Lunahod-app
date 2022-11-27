import typing as t
import abc
from threading import Thread
from dataclasses import dataclass
from datetime import datetime

from inputs import GamePad, InputEvent


class Joystick(abc.ABC):
    def __init__(self, joystick: GamePad) -> None:
        self._joystick = joystick
        self._event_tuples: list[EventTuple] = []

        self._start_threads()

    def add_event(self, event_tuple: "EventTuple"):
        self._event_tuples.append(event_tuple)

    def _start_threads(self) -> None:
        self._monitor_thread = Thread(target=self._controller_thread, daemon=True)
        self._monitor_thread.start()

    def _controller_thread(self):
        while True:
            for joystick_event in self._joystick.read():
                if not(joystick_event.ev_type in ("Absolute", "Key")):
                    continue

                self._start_events_by_joystick_event(joystick_event)

    @abc.abstractmethod
    def _prepare_joystick_event(self, joystick_event: InputEvent) -> "JoystickInput":
        pass

    def _start_events_by_joystick_event(self, joystick_event: InputEvent) -> None:
        for event in self._filter_events_by_code(joystick_event.code):
            event.do(event=self._prepare_joystick_event(joystick_event))

    def _filter_events_by_code(self, code: str) -> list["JoystickEvent"]:
        return [
            event_tuple.event
            for event_tuple in self._event_tuples
            if code in event_tuple.codes
        ]


class JoystickEvent(abc.ABC):
    def do(self, event: "JoystickInput") -> None:
        if event.state != 0:
            self.on_pressed(event)
        else:
            self.on_release(event)

    def on_pressed(self, event: "JoystickInput"):
        pass

    def on_release(self, event: "JoystickInput"):
        pass

@dataclass
class JoystickInput():
    device: GamePad
    timestamp: datetime
    code: str
    state: float


class EventTuple(t.NamedTuple):
    codes: list[str]
    event: "JoystickEvent"
