from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('account/admin', views.admin, name='admin'),
    path('account/admin/AddViewer', views.adminAdd, name='adminAdd'),
]
