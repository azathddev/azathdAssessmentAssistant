from typing import Annotated, final
from uuid import UUID

import msgspec

from server.apps.main.logic.constants import GAME_TITLE_MAX_LENGTH


class GameCreatePayload(msgspec.Struct):
    """Used to create ``Game`` models."""

    title: Annotated[
        str,
        msgspec.Meta(min_length=1, max_length=GAME_TITLE_MAX_LENGTH),
    ]
    mode_formula: str


@final
class GameFullPayload(GameCreatePayload):
    """Used to represent existing ``Game`` models."""

    id: int


class AppointmentCreatePayload(msgspec.Struct):
    """Used to create ``Appointment`` models."""

    game_id: int
    user_id: int
    is_active: bool | None


@final
class AppointmentFullPayload(AppointmentCreatePayload):
    """Used to represent existing ``Appointment`` models."""
    id: int
