from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    #path("new/<int:new>&<str:player>", views.joingame, name="joingame"),
    path("join", views.joingame, name="joingame"),
    path("play", views.play, name="play"),
    path("newround", views.newround, name="newround"),
]