"""Command-line entry point for the demo fixture."""
from __future__ import annotations

import argparse

from .formatting import render_tasks
from .seed import demo_board


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Show the Pull Guard demo board.")
    parser.add_argument("--status", choices=("todo", "doing", "done"), help="Show one workflow column")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    board = demo_board()
    print(render_tasks(board.list(status=args.status)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
