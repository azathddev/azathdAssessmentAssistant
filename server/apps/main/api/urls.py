from dmr.routing import path

from server.apps.main.api import views

app_name = 'main'

urlpatterns = [
    path('games/', views.GameCreate.as_view(), name='game_create'),
    path('games/<int:id>', views.GameGet.as_view(), name='game_get'),
    path('appointments/<int:id>', views.AppointmentGet.as_view(), name='appointment_get'),
    path('appointments/', views.AppointmentCreate.as_view(), name='appointment_create'),
]
