import abc
from threading import Thread
from dataclasses import dataclass
from datetime import datetime

from inputs import GamePad, InputEvent


class Joystick(abc.ABC):
    def __init__(self, joystick: GamePad) -> None:
        self._joystick = joystick
        self._events: list["ABCJoystickEvent"] = []

        self._start_threads()

    def set_event(self, event: "ABCJoystickEvent"):
        self._events.append(event)

    def _start_threads(self) -> None:
        self._monitor_thread = Thread(target=self._controller_thread, daemon=True)
        self._monitor_thread.start()

    def _controller_thread(self):
        while True:
            self._read_joystick_events(self._joystick.read())

    @abc.abstractmethod
    def _prepare_joystick_event(self, joystick_event: InputEvent) -> "JoystickInput":
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
                event.on_event(self._prepare_joystick_event(joystick_event))


class ABCJoystickEvent(abc.ABC):
    def on_event(self, event: "JoystickInput") -> None:
        pass


@dataclass
class JoystickInput():
    device: GamePad
    timestamp: datetime
    code: str
    state: int
