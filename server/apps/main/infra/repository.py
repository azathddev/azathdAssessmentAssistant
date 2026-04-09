from __future__ import annotations

from typing import final

import attrs

from server.apps.main.logic.value_objects import GameCreatePayload
from server.apps.main.models import Game


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
