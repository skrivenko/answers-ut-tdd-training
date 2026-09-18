import pytest
from app import *
from app.Exceptions.invalid_operation_exception import InvalidOperationException
from app.Exceptions.too_many_players_exception import TooManyPlayersException


def test_player_is_in_game_when_he_joined_game():
    player = player_joined_game()

    assert player.is_in_game()


def test_player_can_not_join_game_twice():
    game = RollDiceGame()
    player = player_joined(game)  
    with pytest.raises(InvalidOperationException) as exception:
        player.join(game)

    assert exception is not None


def test_seventh_player_can_not_join_game_since_six_is_max():
    game = game_with_six_players()
    player = Player()
    with pytest.raises(TooManyPlayersException) as exception:
        player.join(game)

    assert exception is not None


def test_player_is_not_in_game_when_he_joined_and_left_game():
    player = player_joined_game()
    player.leave_game()

    assert not player.is_in_game()


def test_player_can_not_leave_game_if_he_did_not_join_it():
    player = Player()
    with pytest.raises(InvalidOperationException) as exception:
        player.leave_game()

    assert exception is not None


def test_player_has_chips_when_he_bought_them():
    player = player_joined_game()
    player.buy(Chip(5))

    assert player_has_exactly_chips(player, Chip(5))
    

def test_player_can_not_bet_if_he_did_not_buy_chips():
    player = Player()  
    game = game_with_player(player)

    with pytest.raises(InvalidOperationException) as exception:
        game.bet(player, Bet(Chip(3), 7))

    assert exception is not None
    

def test_player_looses_when_he_played_non_existing_score():
    player = player_with_five_chips()
    game = game_with_player(player)

    game.bet(player, Bet(Chip(3), 7))
    game.play()

    assert player_has_exactly_chips(player, Chip(2))


### private functions to set up test data and to assert

def player_joined_game() -> player:
    game = RollDiceGame()
    return player_joined(game)


def player_joined(game: RollDiceGame) -> player:
    player = Player()  
    player.join(game)
    return player


def player_with_five_chips() -> player:
    player = Player()  
    player.buy(Chip(5))
    return player


def game_with_player(player: Player) -> roll_dice_game:
    game = RollDiceGame()
    player.join(game)
    return game


def game_with_six_players() -> roll_dice_game:
    game = RollDiceGame()
    for i in range(0, 6): 
        player = Player() 
        player.join(game) 
    return game


def player_has_exactly_chips(player: Player, chips: Chip) -> bool:
    return player.has(chips) and not player.has(chips + Chip(1))   

