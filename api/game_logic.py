import random


class TicTacToeGame:

    def __init__(self, size=3):
        self.board = [[" " for _ in range(size)] for _ in range(size)]
        self.current_player = "X"
        self.moves = []
        self.game_winner = None
        self.size = size

    def make_move(self, x, y):
        if self.board[x][y] == " ":
            self.board[x][y] = self.current_player
            self.moves.append({"player": self.current_player, "x": x, "y": y})
            self.current_player = "O" if self.current_player == "X" else "X"
            return True
        return False

    def random_move(self):
        empty_cells = [
            (x, y)
            for x in range(self.size)
            for y in range(self.size)
            if self.board[x][y] == " "
        ]
        if empty_cells:
            x, y = random.choice(empty_cells)
            self.make_move(x, y)
            return True

    def check_winner(self):
        pass
