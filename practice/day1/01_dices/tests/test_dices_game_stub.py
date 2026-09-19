from app import *


def test_player_looses_when_he_played_non_winning_score():
    player = player_with_five_chips()
    game = game_with_bet(player, bet_with_three_chips(2))
    Dice.roll = staticmethod(lambda: 5)
    
    game.play()
    assert player_has_exactly_chips(player, Chip(2))


def test_player_wins_when_he_played_winning_score():
    player = player_with_five_chips()
    game = game_with_bet(player, bet_with_three_chips(5))
    Dice.roll = staticmethod(lambda: 5)
    
    game.play()
    assert player_has_exactly_chips(player, Chip(2 + 3 * 6))


# private functions to set up test data and to assert

def player_with_five_chips() -> Player:
    player = Player()
    player.buy(Chip(5))
    return player


def game_with_bet(player: Player, bet: Bet) -> RollDiceGame:
    game = RollDiceGame()
    player.join(game)
    game.bet(player, bet)
    return game


def bet_with_three_chips(score: int) -> Bet:
    return Bet(Chip(3), score)


def player_has_exactly_chips(player: Player, chips: Chip) -> bool:
    return player.has(chips) and not player.has(chips + Chip(1))


