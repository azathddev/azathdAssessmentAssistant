from __future__ import annotations

from typing import TYPE_CHECKING, final

import attrs

from server.apps.auth.logic.value_objects import (
    UserLoginPayload,
    UserCredentialsPayload,
)

if TYPE_CHECKING:
    from server.apps.auth.infra import mappers, repository
    import server.apps.auth.logic.services.auth_service as service


@final
@attrs.define(slots=True, frozen=True)
class LoginUser:
    """Creates ``User`` instances."""

    _service: service.AuthService
    _repository: repository.UserRepo
    _mapper: mappers.UserLoginMapper

    def __call__(
        self,
        parsed_body: UserLoginPayload,
    ) -> UserCredentialsPayload:
        """
        There's no real story to tell about this example.

        But here you need to put a text description of what business
        needs to be done in this usecase.
        """
        return self._mapper(self._service.login(parsed_body))
