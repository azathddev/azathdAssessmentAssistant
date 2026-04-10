from dmr.routing import path

from server.apps.auth.api import views

app_name = 'auth'

urlpatterns = [
    path('auth/login/', views.UserLogin.as_view(), name='user_login'),
    path('auth/register/', views.UserRegister.as_view(), name='user_register'),
]
