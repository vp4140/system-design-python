
class PieceType:
    X="X"
    O="O"

class Piece:
    pass

class PlayingPiece:
    def __init__(self,piece):
        self.piece_type = piece

class PieceX(PlayingPiece):
    def __init__(self):
        super().__init__(PieceType.X)

class PieceO(PlayingPiece):
    def __init__(self):
        super().__init__(PieceType.O)

class Player:
    def __init__(self,name,playingpiece:PlayingPiece):
        self.name = name
        self.playingpiece = playingpiece

class Board:
    def __init__(self,size):
        self.size = size
        self.grid = [[None for _ in range(size)] for _ in range(size)]

    def fill_board(self,r,c,playingpiece:PlayingPiece):
        ROWS = len(self.grid)
        COLS = len(self.grid[0])
        if r not in range(ROWS) and c not in range(COLS):
            print("Enter valid indexes")
            return False
        if self.grid[r][c] is not None:
            print("posotion already filled")
            return False
        print(playingpiece)
        self.grid[r][c] = playingpiece
        self.displayBoard()
        print("Added succesfully")
        return True

    def check_winner(self):
        ROWS = len(self.grid)
        COLS = len(self.grid[0])
        for r in range(ROWS):
            counter = 0
            for c in range(COLS):
                if self.grid[r][c] == PieceType.O:
                    counter+=1
            if counter == COLS:
                return True


            counter = 0
            for c in range(COLS):
                if self.grid[r][c] == PieceType.X:
                    counter+=1
            if counter == COLS:
                return True

        for c in range(COLS):
            counter = 0
            for r in range(ROWS):
                if self.grid[r][c] ==  PieceType.O:
                    counter +=1
                if counter == ROWS:
                    return True

            counter = 0
            for r in range(ROWS):
                if self.grid[r][c] == PieceType.X:
                    counter += 1
                if counter == ROWS:
                    return True

        return  False

    def is_full(self):
        ROWS = len(self.grid)
        COLS = len(self.grid[0])
        counter = 0
        for r in range(ROWS):
            for c in range(COLS):
                if self.grid[r][c] is not None:
                    counter +=1
        if counter == ROWS * COLS:
            return True
        else:
            return False

    def displayBoard(self):
        ROWS = len(self.grid)
        COLS = len(self.grid[0])

        for r in range(ROWS):
            print(self.grid[r])


class TicTacToeGame:
    def __init__(self,player1:Player,player2:Player,size):
        self.board = Board(size)
        self.players = [player1,player2]
        self.current_player_index = 0

    def start_game(self):
        while True:
            # self.board.displayBoard()
            current_player = self.players[self.current_player_index]
            r, c = map(int, input("Enter row and column (0-indexed): ").split())
            if self.board.fill_board(r,c,current_player.playingpiece.piece_type):
                if self.board.check_winner():
                    print("Plyer"+current_player.name+"is the winner")
                    return
                if self.board.is_full():
                    print("Is full")
                    print("Its a tie")
                    return
                self.current_player_index = 1 - self.current_player_index

            else:
                print("Something went wrong here")


if __name__ == "__main__":

    X = PieceX()
    O = PieceO()

    Player1 = Player("Vishal",X)
    Player2 = Player("Honey", O)

    obj = TicTacToeGame(Player1,Player2,3)
    obj.start_game()













