from app.player import Player
from app.roll_dice_game import RollDiceGame
from tests.builders.create_player import CreatePlayer


class CreateGame:
    _game: RollDiceGame

    def __init__(self):
        self._game = RollDiceGame()
    

    def with_six_players(self):
        for i in range(0, 6): 
            CreatePlayer().joined_game(self._game)
        return self
    
    
    def please(self):
        return self._game
    
    

