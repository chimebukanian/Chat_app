from django.urls import path
from .  import views

app_name='chatapplication'

urlpatterns = [
    path('', views.index, name='index')
]