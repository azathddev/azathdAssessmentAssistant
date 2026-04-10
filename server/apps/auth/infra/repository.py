from __future__ import annotations

from typing import final

import attrs

from server.apps.auth.models import User
from server.apps.auth.logic.value_objects import UserRegisterPayload, UserFullPayload


@final
@attrs.define(slots=True, frozen=True)
class UserRepo:
    """Repository for the ``User`` model."""

    def create(self, parsed_body: UserRegisterPayload) -> User:
        """Creates new ``Game`` model."""
        return User.objects.create_user(
            **parsed_body.__dict__
        )

    def get_by_id(self, user_id: int) -> User:
        """Return ``User`` model by the primary key."""
        return User.objects.get(pk=user_id)

    def get_by_username(self, username: str) -> User:
        """Return ``User`` model by the primary key."""
        return User.objects.get(username=username)
