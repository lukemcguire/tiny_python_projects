#!/usr/bin/env python3
"""
Author : Luke McGuire <luke.mcguire@gmail.com>
Date   : 2024-07-03
Purpose: Tic-Tac-Toe
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Tic-Tac-Toe",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "-b",
        "--board",
        help="The state of the board",
        metavar="board",
        type=str,
        default="." * 9,
    )

    parser.add_argument(
        "-p",
        "--player",
        help="Player",
        metavar="player",
        type=str,
        choices=["X", "O"],
        default=None,
    )

    parser.add_argument(
        "-c",
        "--cell",
        help="Cell 1-9",
        metavar="cell",
        type=int,
        choices=range(1, 10),
        default=None,
    )

    args = parser.parse_args()

    if len(args.board) != 9 or any(c not in "XO." for c in args.board):
        parser.error(f'--board "{args.board}" must be 9 characters of ., X, O')

    if any([args.player, args.cell]) and not all([args.player, args.cell]):
        parser.error("Must provide both --player and --cell")

    if args.cell and args.board[args.cell - 1] != ".":
        parser.error(f'--cell "{args.cell}" already taken')

    return args


# --------------------------------------------------
def format_board(board: str) -> str:
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
def find_winner(board):
    """Determine if there is a winner"""

    wins = [
        ("PPP......"),
        ("...PPP..."),
        ("......PPP"),
        ("P..P..P.."),
        (".P..P..P."),
        ("..P..P..P"),
        ("P...P...P"),
        ("..P.P.P.."),
    ]

    for player in "XO":
        for winning_board in wins:
            if is_winning(board, winning_board, player):
                return player

    return None


# --------------------------------------------------
def is_winning(board, condition, player):
    """Check if the board matches a win condition"""
    condition = condition.replace("P", player)
    for win_cell, board_cell in zip(condition, board):
        if win_cell not in (".", board_cell):
            return False
    return True


# --------------------------------------------------


def main():
    """Make a jazz noise here"""

    args = get_args()
    board = args.board
    if args.cell:
        board = board[: args.cell - 1] + args.player + board[args.cell :]

    winner = find_winner(board)
    print(format_board(board))
    print(f"{winner} has won!" if winner else "No winner.")


# --------------------------------------------------
if __name__ == "__main__":
    main()
