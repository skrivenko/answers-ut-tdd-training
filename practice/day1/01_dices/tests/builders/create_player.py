from app.chip import Chip
from app.player import Player
from app.roll_dice_game import RollDiceGame


class CreatePlayer:
    _player: Player

    def __init__(self):
        self._player = Player()
    

    def joined_game(self, game : RollDiceGame):
        self._player.join(game)
        return self
    
    
    def with_five_chips(self):
        self._player.buy(Chip(5))
        return self
    
    
    def please(self):
        return self._player
    
    

