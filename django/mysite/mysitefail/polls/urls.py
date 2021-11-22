from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    #Should there be a comma at the end of the line of it's the only line?
    path('', views.index, name='index'),
]