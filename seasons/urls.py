from django.urls import path
from . import views

app_name = 'seasons'
urlpatterns = [
    path('', views.index, name='home'),
    path('update_team_wins/', views.update_team_wins, name='update_team_wins')
]
