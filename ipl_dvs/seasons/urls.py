from django.urls import path
from . import views

app_name = 'seasons'
urlpatterns = [
    path('', views.index, name='home'),
]
