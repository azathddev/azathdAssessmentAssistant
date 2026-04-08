from http import HTTPStatus
from typing import final, override

from django.http import HttpResponse
from dmr import Body, Controller, modify
from dmr.endpoint import Endpoint
from dmr.errors import ErrorType
from dmr.metadata import ResponseSpec
from dmr.plugins.msgspec import MsgspecSerializer

from server.apps.main.logic.usecases import game_create, game_get
from server.apps.main.logic.value_objects import (
    GameCreatePayload,
    GameFullPayload,
)
from server.apps.main.models import Game
from server.common.di import HasContainer


@final
class GameCreate(
    HasContainer,
    Controller[MsgspecSerializer],
):
    """Top level endpoints for the ``Game`` model."""

    def post(
        self,
        parsed_body: Body[GameCreatePayload],
    ) -> GameFullPayload:
        """Create new ``Game`` model."""
        return self.resolve(game_create.CreateGame)(parsed_body)


@final
class GameGet(
    HasContainer,
    Controller[MsgspecSerializer],
):
    """Endpoints that only require a path for ``Game`` models."""

    @modify(
        extra_responses=[
            ResponseSpec(
                Controller.error_model,
                status_code=HTTPStatus.NOT_FOUND,
            ),
        ],
    )
    def get(self) -> GameFullPayload:
        """Return existing ``Game`` model by id."""
        return self.resolve(game_get.GetGame)(self.kwargs['id'])

    @override
    def handle_error(
        self,
        endpoint: Endpoint,
        controller: Controller[MsgspecSerializer],
        exc: Exception,
    ) -> HttpResponse:
        """Handle specific errors for this controller."""
        # Since it is the only error that can happen here,
        # we don't reach full coverage:
        if isinstance(exc, Game.DoesNotExist):  # pragma: no branch
            return self.to_error(
                self.format_error(
                    'Blog post not found',
                    error_type=ErrorType.not_found,
                ),
                status_code=HTTPStatus.NOT_FOUND,
            )
        return super().handle_error(  # pragma: no cover
            endpoint,
            controller,
            exc,
        )
