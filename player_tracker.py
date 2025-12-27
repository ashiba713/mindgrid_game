class PlayerTracker:
    def __init__(self):
        self.moves = []

    def log_move(self, index):
        self.moves.append(index)

    def aggression_level(self):
        return len(set(self.moves))
