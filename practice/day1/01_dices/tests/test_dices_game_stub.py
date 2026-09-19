from app import *


def test_player_looses_when_he_played_non_winning_score():
    player = player_with_five_chips()
    game = game_with_bet(player, 2)
    Dice.roll = staticmethod(lambda: 5)
    
    game.play()
    
    assert player_has_exactly_chips(player, Chip(2))


def test_player_wins_when_he_played_winning_score():
    player = player_with_five_chips()
    game = game_with_bet(player, 5)
    Dice.roll = staticmethod(lambda: 5)
    
    game.play()
    
    assert player_has_exactly_chips(player, Chip(2 + 3 * 6))


# private functions to set up test data and to assert

def player_with_five_chips() -> Player:
    player = Player()
    player.buy(Chip(5))
    return player


def game_with_bet(player: Player, score: int) -> RollDiceGame:
    game = RollDiceGame()
    player.join(game)
    game.bet(player, Bet(Chip(3), score))
    return game


def player_has_exactly_chips(player: Player, chips: Chip) -> bool:
    return player.has(chips) and not player.has(chips + Chip(1))


