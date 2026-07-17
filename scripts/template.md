# Hi, I'm Leo

CS sophomore at Rice, originally from New Zealand. I build things and write down what broke along the way. Current projects: [blundernet](https://github.com/leozh0u/blundernet), a chess engine that retrains itself on a schedule; [relayq](https://github.com/leozh0u/relayq), a crash-safe Rust job queue I test by SIGKILLing its workers mid-job; [bare-metal STM32 motor firmware](https://github.com/leozh0u/stm32-bldc-motor-controller) written straight against the reference manual; and [quant-signals](https://github.com/leozh0u/quant-signals), a signal-research rig that so far mostly proves my trading ideas stop working once you charge them transaction costs. More on my [portfolio site](https://leozh0u.github.io/leo-portfolio/).

For fun: fencing (I competed for New Zealand for a long time), drums, chess, GeoGuessr, and drawing. I love Lego, own a collection I'm genuinely proud of, and hold lasting nostalgia for Ninjago and The Lego Batman Movie. I've also sunk a lot of hours into Minecraft: was very good at Bedwars, still a sweaty SMP grinder, and I've gone down the speedrunning rabbit hole too.

## Play chess against my engine

This is a live game against [BlunderNet](https://github.com/leozh0u/blundernet), a small AlphaZero-style network I train continuously on free CI hardware. The whole internet shares the White pieces. BlunderNet plays Black on its own.

**To move:** click a move under the board, then press **Create** on the issue that opens. That's it. A workflow hands your move to the engine and the board here updates with its reply in a minute or two.

<img src="{{BOARD_URL}}" width="400" alt="current board">

{{STATUS}}

{{MOVES}}

<details>
<summary>Moves so far, scoreboard, recent players</summary>

**This game:** {{MOVELIST}}

**All-time score:** {{SCORE}}

**Recent players:** {{RECENT}}

</details>

### How it works

Each move link opens a pre-filled GitHub issue. A workflow validates the move against the current position, runs MCTS over the latest [released checkpoint](https://github.com/leozh0u/blundernet/releases/tag/model-latest), commits the new board, and closes the issue with the engine's reply. When a game ends, the result lands on the scoreboard and a fresh game starts. All the code is in [scripts/](scripts/).

Fair warning: the engine is young. Its first Stockfish anchor put it near 1000 Elo, so beating it is expected. It retrains every day, though. The scoreboard will show when that stops being funny.
