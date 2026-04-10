from dmr.routing import path

from server.apps.auth.api import views

app_name = 'auth'

urlpatterns = [
    path('auth/login/', ..., name='user_login'),
    path('auth/register/', ..., name='user_register'),
]
