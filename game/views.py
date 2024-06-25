from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.template import loader
from django import forms

from game.data import GameManager

def index(request):#join or create a game
    template = loader.get_template("game/index.html")
    game_id = request.GET.get('game_id', "")
    gm : GameManager = GameManager.get()
    context = {
        "game_id": game_id,
        "joining": game_id != "" and int(game_id) in gm.games 
    }
    return render(request, "game/index.html", context)

def joingame(request):#redirects after adding player to a game or creating a new game
    game_id = int(request.GET.get('game_id', -1))
    player : str = request.GET.get('name')
    player = player.strip().lower().replace(" ", "_")
    new = game_id == -1
    gm : GameManager = GameManager.get()
    if new:
        game_id = gm.initializeGame(player)
    else:
        player = gm.joinGame(game_id, player)
    
    response = redirect("play")
    response["Location"] += f"?game_id={game_id}&name={player}"
    return response
    #return HttpResponse(f"{'Creating' if new else 'Joining'} game {game_id} as {player} playing:{gm.getPlayers(game_id)}")


def play(request):#play with assigned role in game_id
    game_id = int(request.GET.get('game_id', -1))
    player = request.GET.get('name')
    if player is None:
        return HttpResponse("Missing arguments")
    gm : GameManager = GameManager.get()
    context = {
        "game_id": game_id,
        "name": player,
        "players": ", ".join(gm.getPlayers(game_id)),
        "round": gm.getRound(game_id),
        "imbroglione": gm.getImbroglione(game_id).lower() == player.lower(),
        "creator": gm.getCreatingPlayer(game_id) == player,
        "secret_word": gm.getSecret(game_id),
        "suggestion" : gm.getHint(game_id)
    }
    return render(request, "game/play.html", context)

def newround(request):#join or create a game
    game_id = int(request.GET.get('game_id', -1))
    gm : GameManager = GameManager.get()
    return  HttpResponse(gm.newRound(game_id))