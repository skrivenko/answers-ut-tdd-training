import pytest
from app import *


@pytest.fixture(scope="function")
def player():
    return Player()  


@pytest.fixture(scope="function")
def game():
    return RollDiceGame()  


@pytest.fixture(scope="function")
def player_joined_game():
    game = RollDiceGame()
    player = Player()  
    player.join(game)
    return player


@pytest.fixture(scope="function")
def player_with_five_chips():
    player = Player()  
    player.buy(Chip(5))
    return player


@pytest.fixture(scope="function")
def game_with_six_players():
    game = RollDiceGame()
    for i in range(0, 6): 
        player = Player() 
        player.join(game) 
    return game


@pytest.fixture(scope="module")
def has_player_exactly_chips():
    def _has_player_exactly_chips(player: Player, chips: Chip) -> bool:
        return player.has(chips) and not player.has(chips + Chip(1))    
    return _has_player_exactly_chips
