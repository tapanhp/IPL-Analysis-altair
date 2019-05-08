from django.urls import path
from . import views

app_name = 'players'
urlpatterns = [
    path('', views.index, name='home'),
    path('update_batsman_vs_team/', views.update_batsman_vs_team, name='update_batsman_vs_team'),
    path('update_batsman_vs_season/', views.update_batsman_vs_season, name='update_batsman_vs_season'),
    path('update_batsman_vs_stadium/', views.update_batsman_vs_stadium, name='update_batsman_vs_stadium'),
]
