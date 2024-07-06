#!/usr/bin/env python3
"""
Author : Luke McGuire <luke.mcguire@gmail.com>
Date   : 2024-07-06
Purpose: Interactive Tic-Tac-Toe
"""

import os
from typing import List, NamedTuple, Optional


# --------------------------------------------------
class State(NamedTuple):
    """Holds the state information for the Tic-Tac-Toe game"""

    board: List[str] = list("." * 9)
    player: str = "X"
    quit: bool = False
    draw: bool = False
    error: Optional[str] = None
    winner: Optional[str] = None


# --------------------------------------------------
def clear() -> None:
    """Clear the terminal screen"""
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


# --------------------------------------------------
def get_move(state: State) -> State:
    """Get the next move from user input"""

    player = state.player
    cell = input(f"Player {player} What is your move? [q to quit]: ")

    if cell == "q":
        return state._replace(quit=True)

    if not (cell.isdigit() and int(cell) in range(1, 10)):
        return state._replace(error=f'Invalid cell "{cell}", please use 1-9')

    board = state.board

    idx = int(cell) - 1
    if board[idx] != ".":
        return state._replace(error=f'Cell "{cell}" already taken')

    board[idx] = player
    return state._replace(
        board=board,
        player="O" if player == "X" else "X",
        winner=find_winner(board),
        draw="." not in board,
    )


# --------------------------------------------------
def format_board(board: List[str]) -> str:
    """Formats the board string as a tic-tac-toe grid"""

    row_divider = "-------------"
    cells = [str(i) if c == "." else c for i, c in enumerate(board, start=1)]

    cells_templ = "| {} | {} | {} |"

    return "\n".join(
        [
            row_divider,
            cells_templ.format(*cells[:3]),
            row_divider,
            cells_templ.format(*cells[3:6]),
            row_divider,
            cells_templ.format(*cells[6:9]),
            row_divider,
        ]
    )


# --------------------------------------------------
def find_winner(board: List[str]) -> Optional[str]:
    """Determine if there is a winner"""
    winning = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6],
    ]

    for player in ["X", "O"]:
        for i, j, k in winning:
            combo = [board[i], board[j], board[k]]
            if combo == [player, player, player]:
                return player

    return None


# --------------------------------------------------
def main() -> None:
    """Make a jazz noise here"""

    state = State()

    while True:
        clear()
        print(format_board(state.board))

        if state.error:
            print(state.error)
            state = state._replace(error=None)
        elif state.winner:
            print(f"{state.winner} has won!")
            break
        elif state.draw:
            print("All right, we'll call it a draw.")
            break

        state = get_move(state)
        if state.quit:
            print("You lose, loser!")
            break


# --------------------------------------------------
if __name__ == "__main__":
    main()
