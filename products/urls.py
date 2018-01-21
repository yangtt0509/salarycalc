from django.urls import path
from products import views


urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.create, name='create'),
]