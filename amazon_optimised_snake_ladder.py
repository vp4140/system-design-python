import random
from typing import List

class Player:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.position = 1  # Start position

class Snake:
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Ladder:
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Board:
    def __init__(self, size, ladders: List[Ladder], snakes: List[Snake]):
        self.size = size
        self.snakes = {snake.start: snake.end for snake in snakes}
        self.ladders = {ladder.start: ladder.end for ladder in ladders}
        self.end_point = size * size

    def is_winner(self, position):
        return position >= self.end_point

    def get_next_position(self, position):
        if position in self.snakes:
            print(f"Oops! Bitten by a snake at {position}. Sliding down to {self.snakes[position]}.")
            return self.snakes[position]
        if position in self.ladders:
            print(f"Yay! Found a ladder at {position}. Climbing up to {self.ladders[position]}.")
            return self.ladders[position]
        return position

class Game:
    def __init__(self, board: Board, players: List[Player], dice_size=6):
        self.board = board
        self.players = players
        self.dice_size = dice_size
        self.current_player_idx = 0

    def roll_dice(self):
        return random.randint(1, self.dice_size)

    def move_player(self, player, roll):
        new_position = player.position + roll
        if new_position > self.board.end_point:
            print(f"{player.name} rolled {roll} but cannot move beyond {self.board.end_point}.")
            return player.position
        return self.board.get_next_position(new_position)

    def play_game(self):
        print("Starting Snake and Ladder Game!")
        while True:
            player = self.players[self.current_player_idx]
            input(f"{player.name}'s turn. Press Enter to roll the dice...")
            roll = self.roll_dice()
            print(f"{player.name} rolled a {roll}.")
            player.position = self.move_player(player, roll)
            print(f"{player.name} is now at position {player.position}.")

            if self.board.is_winner(player.position):
                print(f"Congratulations {player.name}! You have won the game!")
                break

            self.current_player_idx = (self.current_player_idx + 1) % len(self.players)

if __name__ == "__main__":
    p1 = Player(1, "Vishal")
    p2 = Player(2, "Chinmay")

    # Define snakes and ladders
    ladders = [Ladder(5, 10), Ladder(15, 25)]
    snakes = [Snake(17, 4), Snake(19, 7)]

    # Create board and game
    board = Board(size=10, ladders=ladders, snakes=snakes)
    game = Game(board, [p1, p2])

    # Start the game
    game.play_game()
