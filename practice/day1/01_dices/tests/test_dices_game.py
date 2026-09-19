import pytest
from app import *
from app.Exceptions.invalid_operation_exception import InvalidOperationException
from app.Exceptions.too_many_players_exception import TooManyPlayersException


def test_player_is_in_game_when_he_joined_game():
    game = RollDiceGame()
    player = Player()  

    player.join(game)

    assert player.is_in_game()


def test_player_can_not_join_game_twice():
    game = RollDiceGame()
    player = Player()  
    player.join(game)
     
    with pytest.raises(InvalidOperationException) as exception:
        player.join(game)

    assert exception is not None


def test_seventh_player_can_not_join_game_since_six_is_max():
    game = RollDiceGame()
    for i in range(0, 6): 
        player = Player() 
        player.join(game) 
    player = Player()

    with pytest.raises(TooManyPlayersException) as exception:
        player.join(game)

    assert exception is not None


def test_player_is_not_in_game_when_he_joined_and_left_game():
    game = RollDiceGame()
    player = Player()  
    player.join(game)

    player.leave_game()

    assert not player.is_in_game()


def test_player_can_not_leave_game_if_he_did_not_join_it():
    player = Player()

    with pytest.raises(InvalidOperationException) as exception:
        player.leave_game()

    assert exception is not None


def test_player_has_chips_when_he_bought_them():
    game = RollDiceGame()
    player = Player()  
    player.join(game)

    player.buy(Chip(5))

    assert player.has(Chip(5))
    assert not player.has(Chip(6))
    

def test_player_can_not_bet_if_he_did_not_buy_chips(): 
    game = RollDiceGame()
    player = Player() 
    player.join(game)

    with pytest.raises(InvalidOperationException) as exception:
        game.bet(player, Bet(Chip(3), 7))

    assert exception is not None
    

def test_player_looses_when_he_played_non_existing_score():
    game = RollDiceGame()
    player = Player() 
    player.join(game)
    player.buy(Chip(5))
    game.bet(player, Bet(Chip(3), 7))

    game.play()

    assert player.has(Chip(2))
    assert not player.has(Chip(3))

