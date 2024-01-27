from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django import forms

def index(request):#join or create a game
    template = loader.get_template("game/index.html")
    return HttpResponse(template.render())


def newgame(request):#redirects after creating a game
    return HttpResponse("Creating.")

def joingame(request):#redirects after adding player to a game or creating a new game
    return HttpResponse("Joining.")


def play(request, game_id):#play with assigned role in game_id
    context = {
        "game_id": game_id,
        "imbroglione": True,
        "secret_word": "parolona",
        "suggestion" : "parolina"
    }
    return render(request, "game/play.html", context)
