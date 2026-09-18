
from tests.builders.create_game import CreateGame
from tests.builders.create_player import CreatePlayer


class Create:
    @staticmethod
    def player():
        return CreatePlayer()

    @staticmethod
    def game():
        return CreateGame()