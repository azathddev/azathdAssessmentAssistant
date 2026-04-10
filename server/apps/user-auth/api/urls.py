from dmr.routing import path

from server.apps.auth.api import views

app_name = 'user-auth'

urlpatterns = [
    path('user-auth/login/', views.UserLogin.as_view(), name='user_login'),
    path('user-auth/register/', views.UserRegister.as_view(), name='user_register'),
]
