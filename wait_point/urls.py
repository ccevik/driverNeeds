from django.urls import path
from . import views

urlpatterns = [
    path('', views.wait_point_view, name='the_wait_point'),
]