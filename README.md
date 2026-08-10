# Hi, I'm Leo

CS at Rice, originally from Auckland. I work on backend and infrastructure, mostly in Go and Python.

[**blundernet**](https://github.com/leozh0u/blundernet) is the one I spend the most time on. A Go service fleet that serves my chess engine: game state in Redis, inference pushed onto queue-fed workers so a slow move never blocks an HTTP request, the AWS stack in Terraform. It publishes the latency and availability targets it holds itself to, and a status page saying whether it is currently meeting them.

[**blundernet-engine**](https://github.com/leozh0u/blundernet-engine) is the network behind it. Residual CNN with policy and value heads, PUCT tree search written in Python first and then in C++ through pybind11 for a 1.8x speedup. A scheduled pipeline retrains and re-evaluates it without me. It sits around 1000 Elo, which is bad at chess and fine for a small net that has been learning for a few weeks.

[**quant-signals**](https://github.com/leozh0u/quant-signals) is a backtester built so a signal has to survive being tested honestly. Most of my ideas stopped working once I charged them transaction costs, and the writeups for the dead ones are still in the repo.

[**stm32-bldc-motor-controller**](https://github.com/leozh0u/stm32-bldc-motor-controller) is bare-metal firmware written against the reference manual, no HAL. Left over from starting in electrical engineering before I switched.

More at my [portfolio site](https://leozh0u.github.io/leo-portfolio/).
