from __future__ import annotations

import abc
import typing as t
import enum
from dataclasses import dataclass
from datetime import datetime

from inputs import GamePad

if t.TYPE_CHECKING:
    from ...base import JoystickInput


class ABC_XBox360Device(abc.ABC):
    @abc.abstractmethod
    def process(self, event: JoystickInput) -> XBox360DeviceProcessResult:
        pass


class CommonXBox360Device(ABC_XBox360Device):
    def process(self, event: JoystickInput) -> XBox360DeviceProcessResult:
        new_event = XBox360JoystickInput(
            state=event.state,
            device=event.device,
            code=event.code,
            timestamp=event.timestamp,
        )
        result_type = XBox360ProcessResultType.PRESS if event.state != 0 else XBox360ProcessResultType.REALIZE

        return XBox360DeviceProcessResult(type=result_type, event=new_event)


class TriggerXBox360Device(ABC_XBox360Device):
    _MAX_VALUE = 2**8 - 1

    def process(self, event: JoystickInput) -> XBox360DeviceProcessResult:
        new_event = XBox360JoystickInput(
            state=self._normalize_value(event.state),
            device=event.device,
            code=event.code,
            timestamp=event.timestamp,
        )
        result_type = XBox360ProcessResultType.PRESS if event.state != 0 else XBox360ProcessResultType.REALIZE

        return XBox360DeviceProcessResult(type=result_type, event=new_event)

    def _normalize_value(self, state: int) -> float:
        return state / self._MAX_VALUE


class StickXBox360Device(ABC_XBox360Device):
    _MAX_VALUE = 2**15 - 1

    def process(self, event: JoystickInput) -> XBox360DeviceProcessResult:
        new_event = XBox360JoystickInput(
            state=self._normalize_value(event.state),
            device=event.device,
            code=event.code,
            timestamp=event.timestamp,
        )

        if (
            self._get_coordinate(event.code) == XBox360DeviceStickCoordinate.Y
            and event.state == -1
        ):
            new_event.state = 0
            result_type = XBox360ProcessResultType.REALIZE
        elif event.state == 0:
            result_type = XBox360ProcessResultType.REALIZE
        else:
            result_type = XBox360ProcessResultType.PRESS

        return XBox360DeviceProcessResult(type=result_type, event=new_event)

    def _normalize_value(self, state: int) -> float:
        return state / self._MAX_VALUE

    def _get_coordinate(self, code: str) -> XBox360DeviceStickCoordinate:
        return XBox360DeviceStickCoordinate.Y if code.endswith("Y") else XBox360DeviceStickCoordinate.X


class XBox360ProcessResultType(enum.Enum):
    PRESS = enum.auto()
    REALIZE = enum.auto()


@dataclass
class XBox360DeviceProcessResult():
    type: XBox360ProcessResultType
    event: XBox360JoystickInput


class XBox360DeviceStickCoordinate(enum.Enum):
    X = enum.auto()
    Y = enum.auto()


@dataclass
class XBox360JoystickInput():
    device: GamePad
    timestamp: datetime
    code: str
    state: float
