from datetime import datetime, timedelta

import jwt

from server.apps.auth.infra import repository, mappers
from server.apps.auth.logic.exceptions import UserAlreadyExists, UserNotExists
from server.apps.auth.logic.value_objects import UserRegisterPayload, UserCredentialsPayload, UserLoginPayload
from server.apps.auth.models import User

from server.settings.components import config


class AuthService:
    _repository: repository.UserRepo

    def _generate_jwt_token(self, user: User) -> str:
        """Генерация JWT-токена для пользователя."""
        payload = {
            'user_id': user.id,
            'username': user.username,
            'exp': datetime.now() + timedelta(hours=24),
            'iat': datetime.now(),
        }
        token = jwt.encode(
            payload,
            config("JWT_SECRET"),
            algorithm='HS256'
        )
        return token

    def register(self, payload: UserRegisterPayload) -> User:
        if self._repository.get_by_username(payload.username):
            raise UserAlreadyExists

        return self._repository.create(payload)

    def login(self, payload: UserLoginPayload) -> str:
        user = self._repository.get_by_username(payload.username)
        if not user:
            raise UserNotExists

        return self._generate_jwt_token(user)
