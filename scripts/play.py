"""One ply of the profile game.

Usage: play.py "move|e2e4" "github-username"

Validates the visitor's move against the current position, plays it, gets the
engine's reply, updates game/state.json + game/board.svg, and regenerates
README.md. Writes a markdown reply for the issue comment to game/reply.md.

Exit codes: 0 = move played, 2 = move rejected (reply.md says why).
"""

import json
import sys
import urllib.parse
from datetime import datetime, timezone
from pathlib import Path

import chess
import chess.svg

ROOT = Path(__file__).resolve().parent.parent
STATE = ROOT / "game" / "state.json"
HISTORY = ROOT / "game" / "history.jsonl"
BOARD_SVG = ROOT / "game" / "board.svg"
REPLY = ROOT / "game" / "reply.md"
TEMPLATE = ROOT / "scripts" / "template.md"
README = ROOT / "README.md"

REPO = "leozh0u/leozh0u"


def fresh_state(game_no: int, score: dict) -> dict:
    return {
        "game_no": game_no,
        "fen": chess.STARTING_FEN,
        "moves": [],  # {san, uci, by} - "by" is a username or "blundernet"/"fallback"
        "score": score,
        "updated": "",
    }


def load_state() -> dict:
    if STATE.exists():
        return json.loads(STATE.read_text())
    return fresh_state(1, {"humanity": 0, "blundernet": 0, "draws": 0})


def issue_url(move: chess.Move, san: str) -> str:
    title = urllib.parse.quote(f"move|{move.uci()}")
    body = urllib.parse.quote(
        f"Just press **Create** below to play **{san}**. "
        "The board on my profile updates itself in a minute or two. "
        "Don't edit the title or the move won't count."
    )
    return f"https://github.com/{REPO}/issues/new?title={title}&body={body}"


def move_links(board: chess.Board) -> str:
    """Legal moves as clickable links, grouped and sorted. Promotions are
    auto-queen to keep the list sane."""
    moves = {}
    for m in board.legal_moves:
        if m.promotion and m.promotion != chess.QUEEN:
            continue
        moves[board.san(m)] = m
    cells = [f"[{san}]({issue_url(m, san)})" for san, m in sorted(moves.items())]
    return " · ".join(cells)


def status_line(board: chess.Board, state: dict) -> str:
    if board.is_checkmate():
        return "Checkmate."
    if board.is_stalemate():
        return "Stalemate."
    n = len(state["moves"])
    turn = "White (you)" if board.turn == chess.WHITE else "Black (BlunderNet)"
    check = " You're in check." if board.is_check() else ""
    return f"Game {state['game_no']}, move {n // 2 + 1}. {turn} to play.{check}"


def recent_players(state: dict) -> str:
    seen, names = set(), []
    for mv in reversed(state["moves"]):
        by = mv["by"]
        if by in ("blundernet", "fallback") or by in seen:
            continue
        seen.add(by)
        names.append(f"[@{by}](https://github.com/{by})")
        if len(names) == 5:
            break
    return ", ".join(names) if names else "nobody yet, the board is fresh"


def render(board: chess.Board, state: dict) -> None:
    last = None
    if state["moves"]:
        last = chess.Move.from_uci(state["moves"][-1]["uci"])
    BOARD_SVG.write_text(chess.svg.board(board, lastmove=last, size=400))

    score = state["score"]
    ply = len(state["moves"]) + (state["game_no"] * 1000)
    movelist = " ".join(
        (f"{i // 2 + 1}." if i % 2 == 0 else "") + mv["san"]
        for i, mv in enumerate(state["moves"])
    ) or "(no moves yet)"

    out = TEMPLATE.read_text()
    out = out.replace("{{BOARD_URL}}", f"https://raw.githubusercontent.com/{REPO}/main/game/board.svg?v={ply}")
    out = out.replace("{{STATUS}}", status_line(board, state))
    out = out.replace("{{MOVES}}", move_links(board) if not board.is_game_over() else "")
    out = out.replace("{{MOVELIST}}", movelist)
    out = out.replace("{{SCORE}}", f"Humanity **{score['humanity']}** · BlunderNet **{score['blundernet']}** · Draws **{score['draws']}**")
    out = out.replace("{{RECENT}}", recent_players(state))
    README.write_text(out)

    state["updated"] = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    STATE.write_text(json.dumps(state, indent=2) + "\n")


def finish_game(board: chess.Board, state: dict) -> str:
    """Update the scoreboard, archive the game, reset the board. Returns a
    sentence describing the result."""
    outcome = board.outcome()
    if outcome.winner == chess.WHITE:
        state["score"]["humanity"] += 1
        result = "Humanity wins this one."
    elif outcome.winner == chess.BLACK:
        state["score"]["blundernet"] += 1
        result = "BlunderNet takes the game."
    else:
        state["score"]["draws"] += 1
        result = "Drawn."
    with HISTORY.open("a") as f:
        f.write(json.dumps({
            "game_no": state["game_no"],
            "result": board.result(),
            "moves": [mv["san"] for mv in state["moves"]],
            "players": sorted({mv["by"] for mv in state["moves"] if mv["by"] not in ("blundernet", "fallback")}),
        }) + "\n")
    new = fresh_state(state["game_no"] + 1, state["score"])
    state.clear()
    state.update(new)
    return f"{result} ({outcome.termination.name.lower().replace('_', ' ')}) Game {state['game_no']} is set up and White is to move."


def reject(msg: str) -> None:
    REPLY.write_text(msg + "\n")
    sys.exit(2)


def main() -> None:
    title, player = sys.argv[1], sys.argv[2]

    if not title.startswith("move|"):
        reject("That title doesn't look like a move. Use the move links on my profile README.")
    try:
        move = chess.Move.from_uci(title.split("|", 1)[1].strip())
    except ValueError:
        reject("Couldn't parse that as a move. Use the move links on my profile README rather than typing one in.")

    state = load_state()
    board = chess.Board(state["fen"])
    if board.turn != chess.WHITE:
        reject("It's BlunderNet's move right now. Give it a minute and check the board again.")
    if move not in board.legal_moves:
        reject(
            f"`{move.uci()}` isn't legal in the current position. Someone else "
            "probably moved while your tab was open. Head back to my profile "
            "for the current board."
        )

    lines = []

    san = board.san(move)
    board.push(move)
    state["moves"].append({"san": san, "uci": move.uci(), "by": player})
    state["fen"] = board.fen()
    lines.append(f"You played **{san}**.")

    if board.is_game_over():
        lines.append(finish_game(board, state))
        board = chess.Board(state["fen"])
    else:
        from engine import pick_move
        reply_move, engine_name = pick_move(board)
        reply_san = board.san(reply_move)
        board.push(reply_move)
        state["moves"].append({"san": reply_san, "uci": reply_move.uci(), "by": engine_name})
        state["fen"] = board.fen()
        lines.append(f"BlunderNet answered **{reply_san}**.")
        if board.is_game_over():
            lines.append(finish_game(board, state))
            board = chess.Board(state["fen"])

    render(board, state)
    lines.append(f"Board and move links are fresh on [my profile](https://github.com/leozh0u). Thanks for playing.")
    REPLY.write_text("\n\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
