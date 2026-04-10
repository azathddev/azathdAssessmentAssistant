from django.contrib import admin

from server.apps.user_auth.models import User


# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin[User]):
    """Admin panel for User """
