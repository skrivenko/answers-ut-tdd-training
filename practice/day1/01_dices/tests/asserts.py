from app.player import Player
from app.chip import Chip


class Assert:
    @staticmethod
    def player_has_exactly_chips(player: Player, chips: Chip):
        assert player.has(chips) and not player.has(chips + Chip(1))  
