from mockito import mock, times, verify, when, ANY

from app import *


def test_player_looses_when_he_played_non_winning_score(monkeypatch):
    game = RollDiceGame()
    when(Dice).roll().thenReturn(5)
    player = mocked_player_with_bet(game, 1)

    game.play()

    verify(player, times(1)).take(Chip(3))
    verify(player, times(0)).win(ANY)


def test_player_wins_when_he_played_winning_score(monkeypatch):
    game = RollDiceGame()
    when(Dice).roll().thenReturn(5)
    player = mocked_player_with_bet(game, 5)

    game.play()

    verify(player, times(1)).take(Chip(3))
    verify(player, times(1)).win(Chip(18))


### private functions to set up test data

def mocked_player() -> player:
    player = mock(Player)
    when(player).has(ANY).thenReturn(True)
    when(player).join(ANY).doNothing()
    when(player).take(ANY).doNothing()
    when(player).win(ANY).doNothing()
    return player


def mocked_player_with_bet(game:RollDiceGame, bet_score: int) -> player:
    player = mocked_player()
    player.join(game)
    game.bet(player, Bet(Chip(3), bet_score))
    return player
