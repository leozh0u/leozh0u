"""Set up (or reset) the board and render the README from a fresh state.
Run once when the repo is created; harmless to run again mid-game (it
re-renders from the saved state without touching it)."""

from pathlib import Path

import chess

import play

state = play.load_state()
play.render(chess.Board(state["fen"]), state)
print(f"rendered game {state['game_no']}, fen: {state['fen']}")
