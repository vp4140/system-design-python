from warnings import catch_warnings


class Player:
    def __init__(self,id,name):
        self.id =id
        self.name = name


class Snake:
    def __init__(self,x,y):
        self.startpt =  x
        self.end =y

class Ladder:
    def __init__(self,x,y):
        self.startpt=x
        self.end = y
from typing import  List

class Board:
    def __init__(self,size,ladder : [Ladder],snakes:[Snake]):
        self.snakes = snakes
        self.ladder = ladder
        self.board = [i for i in range(1,size*size+1)]
    def is_winner(self,point):
        return point >= self.board[-1]
    def check_if_snake_mouth(self,point):
        for ele in self.snakes:
            if ele.startpt == point:
                return True
        return False

    def check_if_ladder_start(self,point):
        for ele in self.ladder:
            if ele.startpt == point:
                return True
        return False

    def give_end_snake(self,point):
        for ele in self.snakes:
            if ele.startpt == point:
                return ele.end

    def give_end_of_ladder(self,point):
        for ele in self.ladder:
            if ele.startpt == point:
                return ele.end

class Game:
    def __init__(self,board:Board,player1:Player,player2:Player,dice_size):
        self.board = board
        self.player = [player1,player2]
        self.dice_size = [i for i in range(1,dice_size+1)]
        self.current_pos =[1 for i in range(2)]
        self.current_player_idx = 0

    def playGame(self):
        while True:
            current_player = self.player[self.current_player_idx]
            try:
                ans = int(input(f"Roll a dice beetween 1 to {self.dice_size}"))

                self.current_pos[self.current_player_idx] += ans
                if self.board.is_winner(self.current_pos[self.current_player_idx]):
                    print(current_player.name +" is the winner")
                    return
                if self.board.check_if_snake_mouth(self.current_pos[self.current_player_idx]):
                    end = self.board.give_end_snake(self.current_pos[self.current_player_idx])
                    print(f"player {self.current_player_idx} got eaten by snake")
                    self.current_pos[self.current_player_idx] = end
                if self.board.check_if_ladder_start(self.current_pos[self.current_player_idx]):
                    end = self.board.give_end_of_ladder(self.current_pos[self.current_player_idx])
                    print(f"player {self.current_player_idx} took the ladder")
                    self.current_pos[self.current_player_idx] = end
                print("Player1 pos",self.current_pos[0])
                print("Player2 pos", self.current_pos[1])
                self.current_player_idx = 1 - self.current_player_idx

            except:
                print("Soething went wrong")


if __name__=="__main__":
    p1=Player(1,"Vishal")
    p2 = Player(2, "Chinmay")
    ladder1 = Ladder(5,10)
    snake1 = Snake(6,1)

    board = Board(size=10,ladder= [ladder1],snakes=[snake1])
    obj = Game(board,p1,p2,6)

    obj.playGame()














