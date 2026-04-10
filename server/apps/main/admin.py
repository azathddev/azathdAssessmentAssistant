from django.contrib import admin

from server.apps.main.models import Game, Appointment


@admin.register(Game)
class GameAdmin(admin.ModelAdmin[Game]):
    """Admin panel for Game """


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin[Appointment]):
    """Admin panel for Appointment """
