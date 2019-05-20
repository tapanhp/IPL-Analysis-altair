from django.urls import path
from . import views

app_name = 'teams'
urlpatterns = [
    path('', views.index, name='home'),
    path('update_top_wickets/', views.update_top_wickets, name='top_wickets'),
    path('update_team_vs_team/', views.update_team_vs_team, name='team_vs_team'),
    path('update_win_by_runs/', views.update_win_by_runs, name='win_by_runs'),
    path('update_win_by_wickets/', views.update_win_by_wickets, name='win_by_wickets'),
]
