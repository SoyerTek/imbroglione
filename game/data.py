import random


class GameData:
    game_id = 0
    creating_player = ""
    player_list = []
    current_word = ""
    current_hint =""
    current_round = 0
    
    def __init__(self, id, p_name) -> None:
        self.game_id = id
        self.creating_player = p_name
        self.imbroglione = p_name
        self.newRound()
        self.current_word = "Inizia un nuovo round"
        self.current_hint = "Cosa guardi?"
        
    def newRound(self):
        self.current_word = f"that{self.current_round}"
        self.current_hint = f"this{self.current_round}"
        self.imbroglione = random.choice(self.getPlayers())
        self.current_round+=1
        return self.current_round
        
    def getPlayers(self):
        return [*self.player_list, self.creating_player]

class GameManager:
    _Istance = None
    games = {}
    last_game = 0
    
    @staticmethod
    def get():
        if GameManager._Istance is None:
            GameManager._Istance = GameManager()
        return GameManager._Istance
    
    def initializeGame(self, starting_player):
        self.last_game += 1
        self.games[self.last_game] = GameData(self.last_game, starting_player)
        return self.last_game
    
    def joinGame(self, game_id, player_name, ugly_duplicate=0):
        if game_id in self.games:
            game : GameData = self.games[game_id]
            player_name_ = player_name if ugly_duplicate == 0 else f"{player_name}{ugly_duplicate}"
            if player_name_ not in game.player_list:
                game.player_list.append(player_name_)
                return player_name_
            else:
                return self.joinGame(game_id, player_name, ugly_duplicate+1)            
        else:
            print("ERERRORROROE")
            return "NO"
            
    def newRound(self, game_id):
        if game_id in self.games:
            return self.games[game_id].newRound()
        return -1
            
    def getRound(self, game_id):
        if game_id in self.games:
            return self.games[game_id].current_round
        return "-1"
        
    def getSecret(self, game_id):
        if game_id in self.games:
            return self.games[game_id].current_word
        return "ERRROR"
        
    def getHint(self, game_id):
        if game_id in self.games:
            return self.games[game_id].current_hint
        return "ERRROR"
    
    def getCreatingPlayer(self, game_id):
        if game_id in self.games:
            return self.games[game_id].creating_player
        return "ERRROR"
    
    def getImbroglione(self, game_id):
        if game_id in self.games:
            return self.games[game_id].imbroglione
        return "ERRROR"
    
    def getPlayers(self, game_id):
        if game_id in self.games:
            return self.games[game_id].getPlayers()
        return ["ERRROR"]