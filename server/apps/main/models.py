import textwrap
from typing import final, override

from django.db import models

from server.apps.main.logic.constants import GAME_TITLE_MAX_LENGTH


@final
class Game(models.Model):

    title = models.CharField(max_length=GAME_TITLE_MAX_LENGTH)
    game_uuid = models.UUIDField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Game'
        verbose_name_plural = 'Games'

    @override
    def __str__(self) -> str:
        return textwrap.wrap(self.title, GAME_TITLE_MAX_LENGTH // 4)[0]