import pytest
from app import *
from app.Exceptions.invalid_operation_exception import InvalidOperationException
from app.Exceptions.too_many_players_exception import TooManyPlayersException


def test_player_is_in_game_when_he_joined_game(game, player):
    player.join(game)

    assert player.is_in_game()


def test_player_can_not_join_game_twice(game, player):
    player.join(game)
    with pytest.raises(InvalidOperationException) as exception:
        player.join(game)

    assert exception is not None


def test_seventh_player_can_not_join_game_since_six_is_max(game_with_six_players, player):
    with pytest.raises(TooManyPlayersException) as exception:
        player.join(game_with_six_players)

    assert exception is not None


def test_player_is_not_in_game_when_he_joined_and_left_game(player_joined_game):
    player_joined_game.leave_game()

    assert not player_joined_game.is_in_game()


def test_player_can_not_leave_game_if_he_did_not_join_it(player):
    with pytest.raises(InvalidOperationException) as exception:
        player.leave_game()

    assert exception is not None


def test_player_has_chips_when_he_bought_them(player_joined_game, has_player_exactly_chips):
    player_joined_game.buy(Chip(5))

    assert has_player_exactly_chips(player_joined_game, Chip(5))
    

def test_player_can_not_bet_if_he_did_not_buy_enough_chips(player, game):
    player.join(game)

    with pytest.raises(InvalidOperationException) as exception:
        game.bet(player, Bet(Chip(8), 7))

    assert exception is not None
    

def test_player_looses_when_he_played_non_existing_score(player_with_five_chips, game, 
                                                         has_player_exactly_chips):
    player_with_five_chips.join(game)
    game.bet(player_with_five_chips, Bet(Chip(3), 7))

    game.play()

    assert has_player_exactly_chips(player_with_five_chips, Chip(2))
