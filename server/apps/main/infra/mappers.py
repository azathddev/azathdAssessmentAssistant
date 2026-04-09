from __future__ import annotations

from typing import final

import attrs

from server.apps.main.logic.value_objects import GameFullPayload
from server.apps.main.models import Game


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
