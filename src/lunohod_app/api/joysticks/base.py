import abc
from threading import Thread
from dataclasses import dataclass
from datetime import datetime

from inputs import GamePad, InputEvent


class Joystick(abc.ABC):
    def __init__(self, joystick: GamePad) -> None:
        self._joystick = joystick
        self._events: dict[str, "JoystickEvent"] = {}

        self._start_threads()

    def set_event(self, code: str, event: "JoystickEvent"):
        self._events[code] = event

    def _start_threads(self) -> None:
        self._monitor_thread = Thread(target=self._controller_thread, daemon=True)
        self._monitor_thread.start()

    def _controller_thread(self):
        while True:
            joystick_events = self._joystick.read()
            for joystick_event in joystick_events:
                if not(joystick_event.ev_type in ("Absolute", "Key")):
                    continue
                try:
                    event = self._events[joystick_event.code]
                except KeyError:
                    continue

                joystick_event = self._prepare_joystick_event(joystick_event)
                event.do(joystick_event)

    @abc.abstractmethod
    def _prepare_joystick_event(self, joystick_event: InputEvent) -> "JoystickInput":
        pass


class JoystickEvent(abc.ABC):
    @abc.abstractmethod
    def do(self, event: "JoystickInput") -> None:
        pass


@dataclass
class JoystickInput():
    device: GamePad
    timestamp: datetime
    code: str
    state: float
