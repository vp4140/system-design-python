from abc import ABC, abstractmethod

class Piece(ABC):
    def __init__(self, color):
        self.color = color  # Can be 'black' or 'white'

    @abstractmethod
    def move(self, start, end, board):
        pass
class King(Piece):
    def move(self, start, end, board):
        # King moves one square in any direction (vertically, horizontally, or diagonally)
        if abs(start[0] - end[0]) <= 1 and abs(start[1] - end[1]) <= 1:
            return True
        return False
class Queen(Piece):
    def move(self, start, end, board):
        # Queen moves in a straight line (horizontal, vertical, or diagonal)
        if start[0] == end[0] or start[1] == end[1] or abs(start[0] - end[0]) == abs(start[1] - end[1]):
            return True
        return False
class Rook(Piece):
    def move(self, start, end, board):
        # Rook moves horizontally or vertically
        if start[0] == end[0] or start[1] == end[1]:
            return True
        return False
class Knight(Piece):
    def move(self, start, end, board):
        # Knight moves in an L shape (2 squares in one direction, 1 in the other)
        if (abs(start[0] - end[0]) == 2 and abs(start[1] - end[1]) == 1) or (abs(start[0] - end[0]) == 1 and abs(start[1] - end[1]) == 2):
            return True
        return False
class Bishop(Piece):
    def move(self, start, end, board):
        # Bishop moves diagonally
        if abs(start[0] - end[0]) == abs(start[1] - end[1]):
            return True
        return False
class Pawn(Piece):
    def move(self, start, end, board):
        # Pawn moves one square forward, but two squares on its first move
        if self.color == "white":
            if start[0] == end[0] and end[1] == start[1] + 1:
                return True
            elif start[0] == end[0] and start[1] == 1 and end[1] == 3:
                return True
        elif self.color == "black":
            if start[0] == end[0] and end[1] == start[1] - 1:
                return True
            elif start[0] == end[0] and start[1] == 6 and end[1] == 4:
                return True
        return False


class Board:
    def __init__(self):
        self.board = self.create_board()

    def create_board(self):
        # Initialize an 8x8 board with pieces in their starting positions
        board = [[None] * 8 for _ in range(8)]

        # Place black pieces
        board[0] = [Rook("black"), Knight("black"), Bishop("black"), Queen("black"), King("black"), Bishop("black"),
                    Knight("black"), Rook("black")]
        board[1] = [Pawn("black")] * 8

        # Place white pieces
        board[6] = [Pawn("white")] * 8
        board[7] = [Rook("white"), Knight("white"), Bishop("white"), Queen("white"), King("white"), Bishop("white"),
                    Knight("white"), Rook("white")]

        return board

    def print_board(self):
        for row in self.board:
            print(" ".join([str(piece.__class__.__name__[0]) if piece else "." for piece in row]))

    def is_valid_move(self, start, end, piece):
        # Check if a move is valid
        if not (0 <= start[0] < 8 and 0 <= start[1] < 8 and 0 <= end[0] < 8 and 0 <= end[1] < 8):
            return False  # Out of bounds
        if self.board[start[0]][start[1]] != piece:
            return False  # No piece at the starting position
        if self.board[end[0]][end[1]] and self.board[end[0]][end[1]].color == piece.color:
            return False  # Can't move to a square occupied by a piece of the same color
        return piece.move(start, end, self)

    def move_piece(self, start, end):
        piece = self.board[start[0]][start[1]]
        if self.is_valid_move(start, end, piece):
            self.board[end[0]][end[1]] = piece
            self.board[start[0]][start[1]] = None
            return True
        return False


class Game:
    def __init__(self):
        self.board = Board()
        self.turn = 'white'  # White starts the game

    def play(self):
        self.board.print_board()
        while True:
            print(f"\n{self.turn.capitalize()}'s turn")
            start = tuple(map(int, input("Enter start position (row col): ").split()))
            end = tuple(map(int, input("Enter end position (row col): ").split()))

            piece = self.board.board[start[0]][start[1]]
            if piece and piece.color == self.turn:
                if self.board.move_piece(start, end):
                    self.turn = 'black' if self.turn == 'white' else 'white'
                else:
                    print("Invalid move! Try again.")
            else:
                print("Invalid piece selection or wrong turn! Try again.")

            self.board.print_board()


# Start the game
game = Game()
game.play()
