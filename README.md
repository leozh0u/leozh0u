# Hi, I'm Leo

CS at Rice, originally from Auckland. I work on backend and infrastructure, mostly in Go and Python.

Most of my time goes to [blundernet](https://github.com/leozh0u/blundernet), which is live at [blundernet.com](https://blundernet.com) with about 120 people on it. It is 3.25 million chess puzzles you can filter by rating, theme and phase, plus bots to play against. Drawing a random puzzle out of six million rows took 1.4 seconds with `ORDER BY random()`, so it is a precomputed grid and a stored shuffle key now, which is 0.9ms. The Go API holds no state, inference runs on queue-fed workers so a slow move never blocks a request, and the AWS stack is in Terraform. The engine behind it is [blundernet-engine](https://github.com/leozh0u/blundernet-engine), a small residual net with PUCT search written first in Python and then in C++ through pybind11, retrained on a schedule without me. It plays around 1000 Elo, which is bad at chess and about right for a network this size.

The newer one is [vestigo](https://github.com/leozh0u/vestigo), an agent that works out where a photograph was taken and has to cite evidence for anything it claims. It is scored on calibration rather than distance, because a country it can defend is worth more than a street address it cannot.

The rest of the shelf is older. [quant-signals](https://github.com/leozh0u/quant-signals) is a backtester that mostly proved my trading ideas stop working once I charge them transaction costs, and [stm32-bldc-motor-controller](https://github.com/leozh0u/stm32-bldc-motor-controller) is bare-metal firmware written against the reference manual, left over from starting in electrical engineering. More at my [portfolio site](https://leozh0u.github.io/leo-portfolio/).
