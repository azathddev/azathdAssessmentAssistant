# NOTE: simple layers go on top!

from collections.abc import Callable
from typing import Any

import punq

def _global_namespace() -> dict[str, Any]:
    from django.conf import LazySettings  # noqa: F401
    from django.core.cache import BaseCache  # noqa: F401

    return locals()  # noqa: WPS421


def _create_injector[Thing](
    container: punq.Container,
    localns: dict[str, Any],
) -> Callable[[Thing], Thing]:
    # We need to provide the same string names as we do in the definition.
    localns.pop('container')
    localns.update(_global_namespace())
    container.registrations._localns.update(localns)  # noqa: SLF001
    return lambda service: service


def _inject_django(container: punq.Container) -> None:
    from django.conf import LazySettings, settings

    # Django:
    container.register(
        LazySettings,
        instance=settings,
        scope=punq.Scope.singleton,
    )


def _inject_main(container: punq.Container) -> None:
    from server.apps.main.infra import mappers, repository
    from server.apps.main.logic.usecases.game import game_create, game_get
    from server.apps.main.logic.usecases.appointment import appointment_create, appointment_get

    # Hacks to resolve annotations:
    inject = _create_injector(container, locals())  # noqa: WPS421

    # Things to register:
    container.register(repository.GameRepo)
    container.register(repository.AppointmentRepo)
    container.register(mappers.GameMapper)
    container.register(mappers.AppointmentMapper)

    container.register(inject(game_create.CreateGame))
    container.register(inject(appointment_create.CreateAppointment))
    container.register(inject(game_get.GetGame))
    container.register(inject(appointment_get.GetAppointment))


def _inject_auth(container: punq.Container) -> None:
    from server.apps.auth.infra import mappers, repository
    from server.apps.auth.logic.usecases import user_login, user_register

    # Hacks to resolve annotations:
    inject = _create_injector(container, locals())  # noqa: WPS421

    # Things to register:
    container.register(repository.UserRepo)
    container.register(mappers.UserLoginMapper)
    container.register(mappers.UserRegisterMapper)

    container.register(inject(user_login.LoginUser))
    container.register(inject(user_register.RegisterUser))


def populate_dependencies(container: punq.Container) -> punq.Container:
    """Populates dependencies for the container."""
    # Deps:
    _inject_django(container)
    # Apps:
    _inject_main(container)
    _inject_auth(container)
    return container
