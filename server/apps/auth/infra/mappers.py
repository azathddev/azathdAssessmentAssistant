from __future__ import annotations

from typing import final

import attrs

from server.apps.auth.logic.value_objects import UserFullPayload, UserCredentialsPayload
from server.apps.auth.models import User


@final
@attrs.define(slots=True, frozen=True)
class UserRegisterMapper:
    """Preserves all properties of a ``User``."""

    def __call__(self, user: User) -> UserFullPayload:
        """Map model to a DTO instance."""
        return UserFullPayload(
            id=user.id,
            username=user.username,
            first_name=user.first_name,
            last_name=user.last_name,
            email=user.email
        )

@final
@attrs.define(slots=True, frozen=True)
class UserLoginMapper:
    """Preserves all properties of a ``User``."""

    def __call__(self, token: str) -> UserCredentialsPayload:
        """Map model to a DTO instance."""
        return UserCredentialsPayload(
            access_token=token
        )
