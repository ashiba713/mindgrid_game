import random

class AdaptiveAI:
    def __init__(self):
        self.player_moves = []

    def record_player_move(self, move):
        self.player_moves.append(move)

    def choose_move(self, game):
        # Block frequent player moves
        if self.player_moves:
            common_move = max(set(self.player_moves), key=self.player_moves.count)
            if common_move in game.available_moves():
                return common_move

        # Otherwise random
        return random.choice(game.available_moves())
