#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""A colorful Tic-Tac-Toe game for the terminal."""

import os

RESET = "\033[0m"
RED = "\033[1;31m"
BLUE = "\033[1;34m"


class Board:
    """Game board for Tic-Tac-Toe."""

    def __init__(self):
        self.cells = [" "] * 9

    def display(self):
        """Display the board with colors and cell numbers."""
        def mark(i):
            v = self.cells[i]
            if v == "X":
                return f"{RED}X{RESET}"
            if v == "O":
                return f"{BLUE}O{RESET}"
            return str(i + 1)

        rows = []
        for i in range(0, 9, 3):
            rows.append(" {} | {} | {} ".format(mark(i), mark(i + 1), mark(i + 2)))
        print("\n---+---+---\n".join(rows))

    def update(self, index, mark):
        """Place a mark on the board if the cell is free."""
        if self.cells[index] == " ":
            self.cells[index] = mark
            return True
        return False

    def winner(self):
        """Return 'X', 'O', 'Draw' or None depending on board state."""
        wins = [
            (0, 1, 2),
            (3, 4, 5),
            (6, 7, 8),
            (0, 3, 6),
            (1, 4, 7),
            (2, 5, 8),
            (0, 4, 8),
            (2, 4, 6),
        ]
        for a, b, c in wins:
            if self.cells[a] == self.cells[b] == self.cells[c] != " ":
                return self.cells[a]
        if all(c != " " for c in self.cells):
            return "Draw"
        return None


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


class Game:
    """Main game loop with scoring."""

    def __init__(self):
        self.score = {"X": 0, "O": 0}

    def switch(self, mark):
        return "O" if mark == "X" else "X"

    def get_move(self, mark, board):
        while True:
            try:
                choice = int(input(f"Player {mark}, choose a cell (1-9): ")) - 1
            except ValueError:
                choice = -1
            if 0 <= choice < 9 and board.cells[choice] == " ":
                return choice
            print("Invalid move. Try again.")

    def play_round(self, first):
        board = Board()
        current = first
        while True:
            clear_screen()
            print("Tic-Tac-Toe\n")
            board.display()
            move = self.get_move(current, board)
            board.update(move, current)
            result = board.winner()
            if result:
                clear_screen()
                board.display()
                if result != "Draw":
                    print(f"Player {result} wins!\n")
                    self.score[result] += 1
                else:
                    print("It's a draw!\n")
                break
            current = self.switch(current)
        print(f"Score - X: {self.score['X']} | O: {self.score['O']}\n")

    def play(self):
        first = "X"
        while True:
            self.play_round(first)
            first = self.switch(first)
            again = input("Play again? [y/N]: ").strip().lower()
            if again != "y":
                break


def main():
    Game().play()


if __name__ == "__main__":
    main()
