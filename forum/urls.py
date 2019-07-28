from django.urls import path

from . import views

urlpatterns = [
    path('new/', views.index, name='newforum'),
    path('delete/', views.delete_forum, name='deleteforum'),
]