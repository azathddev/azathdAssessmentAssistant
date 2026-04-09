from __future__ import annotations

from typing import final

import attrs

from server.apps.main.logic.value_objects import GameCreatePayload, AppointmentCreatePayload
from server.apps.main.models import Game, Appointment


@final
@attrs.define(slots=True, frozen=True)
class GameRepo:
    """Repository for the ``Game`` model."""

    def create(self, parsed_body: GameCreatePayload) -> Game:
        """Creates new ``Game`` model."""
        return Game.objects.create(
            title=parsed_body.title,
            mode_formula=parsed_body.mode_formula,
        )

    def get_by_id(self, game_id: int) -> Game:
        """Return ``Game`` model by the primary key."""
        return Game.objects.get(pk=game_id)


@final
@attrs.define(slots=True, frozen=True)
class AppointmentRepo:
    """Repository for the ``Appointment`` model."""

    def create(self, parsed_body: AppointmentCreatePayload) -> Appointment:
        """Creates new ``Game`` model."""
        return Appointment.objects.create(
            game=parsed_body.game_id,
            user=parsed_body.user_id,
        )

    def get_by_id(self, appointment_id: int) -> Appointment:
        """Return ``Appointment`` model by the primary key."""
        return Appointment.objects.get(pk=appointment_id)
