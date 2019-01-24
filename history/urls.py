from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:artist_id>/', views.artist_detail, name='artist_detail'),
]