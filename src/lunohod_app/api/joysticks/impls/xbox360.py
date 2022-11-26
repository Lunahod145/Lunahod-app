from datetime import datetime

from ..base import Joystick, JoystickInput, InputEvent


class XBox360Joystick(Joystick):
    MAX_TRIGGER_VALUE = 2 ** 8
    MAX_JOYSTICK_VALUE = 2 ** 15

    def _prepare_joystick_event(self, joystick_event: InputEvent) -> JoystickInput:
        if joystick_event.code in ("ABS_Y", "ABS_X", "ABS_RY", "ABS_RX"):
            state = self._normalize_trigger_value(joystick_event.state)
        elif joystick_event.code in ("ABS_Z", "ABS_RZ"):
            state = self._normalize_joystick_value(joystick_event.state)
        else:
            state = joystick_event.state

        return JoystickInput(
            device=joystick_event.device,
            timestamp=datetime.fromtimestamp(joystick_event.timestamp),
            code=joystick_event.code,
            state=state,
        )


    def _normalize_trigger_value(self, state: int) -> float:
        return state / self.MAX_TRIGGER_VALUE

    def _normalize_joystick_value(self, state: int) -> float:
        return state / self.MAX_TRIGGER_VALUE
