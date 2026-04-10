from http import HTTPStatus
from typing import final, override

from django.http import HttpResponse
from dmr import Body, Controller, modify
from dmr.endpoint import Endpoint
from dmr.errors import ErrorType
from dmr.metadata import ResponseSpec
from dmr.plugins.msgspec import MsgspecSerializer

from server.apps.auth.logic.value_objects import UserRegisterPayload, UserFullPayload, UserLoginPayload, \
    UserCredentialsPayload
from server.apps.auth.logic.usecases import user_login, user_register
from server.apps.auth.logic.value_objects import (
    UserRegisterPayload, UserFullPayload,
    UserLoginPayload, UserCredentialsPayload
)
from server.apps.auth.models import User
from server.common.di import HasContainer


@final
class UserRegister(
    HasContainer,
    Controller[MsgspecSerializer],
):
    """Top level endpoints for the ``User`` model."""

    def post(
        self,
        parsed_body: Body[UserRegisterPayload],
    ) -> UserFullPayload:
        """Create new ``User`` model."""
        return self.resolve(user_register.RegisterUser)(parsed_body)

@final
class UserLogin(
    HasContainer,
    Controller[MsgspecSerializer],
):
    """Top level endpoints for the ``User`` model."""

    def post(
        self,
        parsed_body: Body[UserLoginPayload],
    ) -> UserCredentialsPayload:
        """ Login user ."""
        return self.resolve(user_login.LoginUser)(parsed_body)

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
        if isinstance(exc, User.DoesNotExist):  # pragma: no branch
            return self.to_error(
                self.format_error(
                    'Login is not success',
                    error_type=ErrorType.not_found,
                ),
                status_code=HTTPStatus.NOT_FOUND,
            )
        return super().handle_error(  # pragma: no cover
            endpoint,
            controller,
            exc,
        )
