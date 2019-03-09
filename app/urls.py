from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="homepage"),
    path('learn-more/', views.index, name="learn_more"),
]
