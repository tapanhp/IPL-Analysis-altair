from django.urls import path
from . import views

app_name = 'players'
urlpatterns = [
    path('', views.index, name='home'),
    path('update_batsman_vs_team/', views.update_batsman_vs_team, name='update_batsman_vs_team')
]
