from django.urls import path
from . import views

app_name = 'players'
urlpatterns = [
    path('', views.index, name='home'),
    path('update_batsman_vs_team/', views.update_batsman_vs_team, name='update_batsman_vs_team'),
    path('update_batsman_vs_season/', views.update_batsman_vs_season, name='update_batsman_vs_season'),
    path('update_batsman_vs_stadium/', views.update_batsman_vs_stadium, name='update_batsman_vs_stadium'),
    path('update_wickets_vs_team/', views.update_wickets_vs_team, name='update_wickets_vs_team'),
    path('update_wickets_vs_season/', views.update_wickets_vs_season, name='update_wickets_vs_season'),
    path('update_season_ddl/', views.update_season_dropdown, name='update_season_ddl'),
    path('update_stadium_ddl/', views.update_stadium_dropdown, name='update_stadium_ddl')
]
