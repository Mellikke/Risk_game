from game.player import Player
from game.game_map import GameMap


class GameEngine:
    def __init__(self):
        self.players = []
        self.game_map = GameMap()
        self.current_player_index = 0

    def setup_game(self):
        self.game_map.create_default_map()

        player1 = Player(1, "Player 1", "Red")
        player2 = Player(2, "Player 2", "Blue")

        self.players.append(player1)
        self.players.append(player2)

        territories = list(self.game_map.territories.values())

        for index, territory in enumerate(territories):
            player = self.players[index % len(self.players)]

            territory.set_owner(player)
            territory.add_armies(3)
            player.add_territory(territory)

        self.start_turn()

    def get_current_player(self):
        return self.players[self.current_player_index]

    def next_turn(self):
        self.current_player_index = (self.current_player_index + 1) % len(self.players)

    def start_turn(self):
        current_player = self.get_current_player()
        current_player.calculate_reinforcements()
        return current_player.reinforcements

    def check_winner(self):
        for player in self.players:
            if len(player.territories) == len(self.game_map.territories):
                return player
        return None