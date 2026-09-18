## Практика
Написать новый unit test на код в упражнении Dice Roll Game
  
**Ответ:**
  
[Код теста](/practice/day1/01_dices/tests/test_dices_game.py)
  
Без детального покрытия метода win, так как тут random.
  
**Комментарий:**
  
В коде есть дополнительная проблема. Метод is_in_game не используется для ставок, и поставить ставку и даже выиграть могут игроки, не присоединившиеся к игре. 
Вариантом исправления (с оговоркой, что игра может быть только одна) может быть дополнение метода bet в RollDiceGame:
```Python
    def bet(self, player: Player, bet: Bet):
        if not player.has(bet.chips):
            raise InvalidOperationException

        if not player.is_in_game():
            raise InvalidOperationException

        self._bets.append({'player': player, 'chips': bet.chips, 'score': bet.score})
        player.take(bet.chips)
```
и написание соответствующего теста:
```Python
def test_player_can_not_bet_if_he_did_not_join_game():
    game = RollDiceGame()
    player = Player()  
    player.buy(Chip(5))

    with pytest.raises(InvalidOperationException) as exception:
        game.bet(player, Bet(Chip(3), 7))

    assert exception is not None
```
