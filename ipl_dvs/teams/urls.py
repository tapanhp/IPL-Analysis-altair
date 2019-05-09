from django.urls import path
from . import views

app_name = 'teams'
urlpatterns = [
    path('', views.index, name='home'),
    path('update_top_wickets/', views.update_top_wickets, name='top_wickets')
]
