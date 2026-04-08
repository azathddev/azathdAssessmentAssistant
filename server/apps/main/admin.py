from django.contrib import admin

from server.apps.main.models import Game


@admin.register(Game)
class BlogPostAdmin(admin.ModelAdmin[Game]):
    """Admin panel for Game """
