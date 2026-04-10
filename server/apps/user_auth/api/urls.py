from dmr.routing import path

from server.apps.user_auth.api import views

app_name = 'user_auth'

urlpatterns = [
    path('user_auth/login/', views.UserLogin.as_view(), name='user_login'),
    path('user_auth/register/', views.UserRegister.as_view(), name='user_register'),
]
