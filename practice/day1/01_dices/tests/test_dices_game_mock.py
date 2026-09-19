from unittest.mock import Mock, patch
from app import *


def test_player_looses_when_he_played_non_winning_score():
    with patch.object(Dice, "roll", return_value=5):
        game = RollDiceGame()
        player = mocked_player_with_bet(game, 1)
        game.play()
    player.take.assert_called_once_with(Chip(3))
    player.win.assert_not_called()


def test_player_wins_when_he_played_winning_score():
    with patch.object(Dice, "roll", return_value=5):
        game = RollDiceGame()
        player = mocked_player_with_bet(game, 5)
        game.play()
    player.take.assert_called_once_with(Chip(3))
    player.win.assert_called_once_with(Chip(18))


# private functions to set up test data

def mocked_player() -> Player:
    player = Mock(spec=Player)
    player.has.return_value = True
    return player


def mocked_player_with_bet(game: RollDiceGame, bet_score: int) -> Player:
    player = mocked_player()
    player.join(game)
    game.bet(player, Bet(Chip(3), bet_score))
    return player
