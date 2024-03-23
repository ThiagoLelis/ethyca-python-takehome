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
            self.moves.append({"id": len(self.moves) + 1, "player": self.current_player, "x": x, "y": y})
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
        for i in range(self.size):
            if all(
                self.board[i][j] == self.board[i][0] and self.board[i][0] != " "
                for j in range(1, self.size)
            ):
                return True, self.board[i][0]

        for j in range(self.size):
            if all(
                self.board[i][j] == self.board[0][j] and self.board[0][j] != " "
                for i in range(1, self.size)
            ):
                return True, self.board[0][j]

        if all(
            self.board[i][i] == self.board[0][0] and self.board[0][0] != " "
            for i in range(1, self.size)
        ):
            return True, self.board[0][0]

        if all(
            self.board[i][j] != " " for i in range(self.size) for j in range(self.size)
        ):
            return True, "Draw"

        return False, None
