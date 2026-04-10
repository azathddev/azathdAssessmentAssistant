from typing import Annotated, final
from uuid import UUID

import msgspec

from server.apps.main.logic.constants import GAME_TITLE_MAX_LENGTH


class UserRegisterPayload(msgspec.Struct):
    """Used to register a ``User`` models."""

    username: str
    password: str
    first_name: str | None
    last_name: str | None
    email: str | None


@final
class UserLoginPayload(msgspec.Struct):
    """Used to log in ``User`` models."""

    username: str
    password: str


@final
class UserFullPayload(UserRegisterPayload):
    """Used to represent existing ``User`` models."""

    id: int


@final
class UserCredentialsPayload(msgspec.Struct):
    """Used to represent existing ``User`` models."""
    access_token: str

