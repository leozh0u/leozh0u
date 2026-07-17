"""Pick BlunderNet's reply. Falls back to a greedy mover if the real engine
can't load, so the game never gets stuck waiting on a fix."""

import os
import sys
from pathlib import Path

import chess

REPO_ROOT = Path(__file__).resolve().parent.parent
MODEL_PATH = REPO_ROOT / "game" / "model.pt"
SIMULATIONS = int(os.environ.get("BLUNDERNET_SIMS", "200"))

PIECE_VALUE = {
    chess.PAWN: 1,
    chess.KNIGHT: 3,
    chess.BISHOP: 3,
    chess.ROOK: 5,
    chess.QUEEN: 9,
}

CENTER = {chess.D4, chess.E4, chess.D5, chess.E5}


def greedy_move(board: chess.Board) -> chess.Move:
    """Mate in one if available, otherwise best capture, otherwise develop
    toward the center. Deterministic tie-break by UCI string."""
    best, best_score = None, float("-inf")
    for move in sorted(board.legal_moves, key=lambda m: m.uci()):
        b = board.copy(stack=False)
        b.push(move)
        if b.is_checkmate():
            return move
        score = 0.0
        if board.is_capture(move):
            victim = board.piece_at(move.to_square)
            if victim is not None:
                score += PIECE_VALUE.get(victim.piece_type, 0)
            elif board.is_en_passant(move):
                score += 1
            # don't trade into a defended square for free
            if b.is_attacked_by(b.turn, move.to_square):
                mover = board.piece_at(move.from_square)
                score -= PIECE_VALUE.get(mover.piece_type, 0) * 0.9
        if move.to_square in CENTER:
            score += 0.3
        if b.is_check():
            score += 0.2
        if score > best_score:
            best, best_score = move, score
    return best


def blundernet_move(board: chess.Board) -> chess.Move:
    """Load the released checkpoint and search. Raises on any problem;
    the caller decides whether to fall back."""
    import torch

    blundernet_src = os.environ.get("BLUNDERNET_SRC")
    if blundernet_src:
        sys.path.insert(0, blundernet_src)
    from blundernet.mcts import best_move
    from blundernet.model import BlunderNet

    model = BlunderNet()
    ckpt = torch.load(MODEL_PATH, map_location="cpu", weights_only=True)
    model.load_state_dict(ckpt["model"])
    model.eval()
    return best_move(board, model, simulations=SIMULATIONS)


def pick_move(board: chess.Board) -> tuple[chess.Move, str]:
    """Returns (move, engine_name). engine_name records which brain moved."""
    try:
        return blundernet_move(board), "blundernet"
    except Exception as exc:  # noqa: BLE001 - any failure means fall back
        print(f"blundernet unavailable, using fallback: {exc}", file=sys.stderr)
        return greedy_move(board), "fallback"
