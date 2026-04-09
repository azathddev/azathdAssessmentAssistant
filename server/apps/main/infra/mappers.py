from __future__ import annotations

from typing import final

import attrs

from server.apps.main.logic.value_objects import GameFullPayload, AppointmentFullPayload
from server.apps.main.models import Game, Appointment


@final
@attrs.define(slots=True, frozen=True)
class GameMapper:
    """Preserves all properties of a ``Game``."""

    def __call__(self, game: Game) -> GameFullPayload:
        """Map model to a DTO instance."""
        return GameFullPayload(
            id=game.id,
            title=game.title,
            mode_formula=game.mode_formula,
        )


@final
@attrs.define(slots=True, frozen=True)
class AppointmentMapper:
    """Preserves all properties of a ``Appointment``."""

    def __call__(self, appointment: Appointment) -> AppointmentFullPayload:
        """Map model to a DTO instance."""
        return AppointmentFullPayload(
            game=appointment.game.id,
            user=appointment.user.id,
            is_active=appointment.is_active
        )
