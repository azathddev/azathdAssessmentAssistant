from dmr.routing import path

from server.apps.main.api import views

app_name = 'main'

urlpatterns = [
    path('games/', views.GameCreate.as_view(), name='game_create'),
    path('games/<int:id>', views.GameGet.as_view(), name='game_get'),
]
