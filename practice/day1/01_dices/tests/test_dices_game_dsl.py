import pytest
from app import *
from app.Exceptions.invalid_operation_exception import InvalidOperationException
from app.Exceptions.too_many_players_exception import TooManyPlayersException
from tests.builders.create import Create
from tests.builders.create_game import CreateGame
from tests.builders.create_player import CreatePlayer
from tests.asserts import Assert

FIVE_CHIPS = Chip(5)
TWO_CHIPS = Chip(2)

THREE_CHIPS_ON_7 = Bet(Chip(3), 7)


def test_player_is_in_game_when_he_joined_game():
    player = Create.player().joined_new_game().please() 

    assert player.is_in_game()


def test_player_can_not_join_game_twice():
    game = RollDiceGame()
    player = Create.player().joined_game(game).please() 

    with pytest.raises(InvalidOperationException) as exception:
        player.join(game)

    assert exception is not None


def test_seventh_player_can_not_join_game_since_six_is_max():
    game = Create.game().with_six_players().please()
    player = Player()

    with pytest.raises(TooManyPlayersException) as exception:
        player.join(game)

    assert exception is not None


def test_player_is_not_in_game_when_he_joined_and_left_game():
    player = Create.player().joined_new_game().please() 
    player.leave_game()

    assert not player.is_in_game()


def test_player_can_not_leave_game_if_he_did_not_join_it():
    player = Player()
    with pytest.raises(InvalidOperationException) as exception:
        player.leave_game()

    assert exception is not None


def test_player_has_chips_when_he_bought_them():
    player = Create.player().joined_new_game().please() 
    player.buy(FIVE_CHIPS)

    Assert.player_has_exactly_chips(player, FIVE_CHIPS)
    

def test_player_can_not_bet_if_he_did_not_buy_chips():
    game = RollDiceGame()
    player = Create.player().joined_game(game).please() 

    with pytest.raises(InvalidOperationException) as exception:
        game.bet(player, THREE_CHIPS_ON_7)

    assert exception is not None
    

def test_player_looses_when_he_played_non_existing_score():
    game = RollDiceGame()
    player = Create.player().joined_game(game).with_five_chips().please() 
    game.bet(player, THREE_CHIPS_ON_7)
    
    game.play()

    Assert.player_has_exactly_chips(player, TWO_CHIPS)

