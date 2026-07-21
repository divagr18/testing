"""Repeatable sample content for demos."""
from .board import Board


def demo_board() -> Board:
    board = Board()
    board.add("Record Pull Guard walkthrough", priority="high")
    board.add("Review overlapping proposals")
    board.add("Publish demo notes", priority="low")
    board.move(1, "doing")
    return board
