class Game:
    def __init__(self):
        self.board = [""] * 9
        self.current_winner = None

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ""]

    def make_move(self, index, player):
        if self.board[index] == "":
            self.board[index] = player
            if self.check_winner(index, player):
                self.current_winner = player
            return True
        return False

    def check_winner(self, index, player):
        row = index // 3
        if all(self.board[row*3 + i] == player for i in range(3)):
            return True

        col = index % 3
        if all(self.board[col + i*3] == player for i in range(3)):
            return True

        if index % 2 == 0:
            if all(self.board[i] == player for i in [0,4,8]):
                return True
            if all(self.board[i] == player for i in [2,4,6]):
                return True

        return False
