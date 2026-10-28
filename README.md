# Hi, I'm Leo

I'm a CS student at Rice, originally from Auckland. I build full-stack software, with a focus on applied AI and backend systems. I'm looking for a Summer 2027 software engineering internship.

Right now I'm building Kasheww at KEWW for a hospitality team's event workflows. Client notes become linked proposals, BEOs and invoices, with Gemini extracting facts for staff to review and ordinary code doing the pricing. There's a Postgres client portal, event-scoped permissions, Gmail and Calendar connections, and an AWS staff beta. Getting a complete event through the staff workflow is the next acceptance step.

I'm also co-developing a Rice Football analytics prototype with RiceApps. My four API routes and typed React preview are merged. The team has added a CFBD client and CSV/JSON import validation, and we're prototyping a library for coaching reports and R/Python analyst scripts.

At Rice, I'm starting LLM routing experiments with Professor Jiarong Xing's group, looking at quality, cost and latency. It's early, so no results yet. My earlier contribution was fixing OAuth refresh, Keychain prompts and SSH usage tracking in TokenGate, a Swift macOS app.

Previously, I automated chip-test reporting at CanSemi with Python, Postgres, FastAPI and a React wafer map. At Inkstone, I worked on ABC Reads, an iOS reader with on-device OCR and a 113,000-entry offline dictionary.

## A few things I've built

### [BlunderNet](https://github.com/leozh0u/blundernet)

A free chess practice site at [blundernet.com](https://blundernet.com), with 3.25 million puzzles, a classroom mode, an engine I trained and Stockfish game review. Random puzzle selection went from 1.4 seconds to 0.9 ms using indexed shuffle keys and size-weighted cells. The backend uses Go, Postgres, Redis and SQS-fed ONNX workers, with Terraform for the AWS deployments. The [engine](https://github.com/leozh0u/blundernet-engine) has a C++ MCTS core alongside its PyTorch model.

### [Vestigo](https://github.com/leozh0u/vestigo)

Works out where a photograph was taken and shows the evidence behind its answer. A street-level answer needs street-level evidence. Its classifier uses frozen SigLIP features and was trained on 64,865 images split by location. It reached 142 km median error and 3.7% calibration error after temperature scaling. Those are classifier results, not end-to-end agent scores. There's a walkthrough at [vestigo.earth](https://vestigo.earth).

### [Perch](https://github.com/leozh0u/perch)

A floating macOS video player I built while practising on Zetamac. Paste a YouTube link, queue some videos and keep watching as you switch apps. Electron and JavaScript, with keyboard controls, global shortcuts and an optional second player.

### [Notch Apple](https://github.com/leozh0u/notch-apple)

My extension of [Boring Notch](https://github.com/TheBoredTeam/boring.notch). I added a native Spotify library browser, PKCE sign-in with Keychain token storage, playback targeted at this Mac, a focus dial and an upcoming-calendar view.

### [From Scratch](https://github.com/leozh0u/from-scratch)

Three of us built this crafting game at HackRice 16. Every recipe cites a source. Start with stone, wood and plant fibre, then work through the chains behind everyday objects. The graph runs offline in the browser; Gemini handles extra explanations. [Play it here](https://leozh0u.github.io/from-scratch/).

I started college in electrical engineering before switching to CS. Outside coding, I fence, play the drums, ski and play chess. More at [leozhou.fyi](https://leozhou.fyi), or reach me at [zhouleo2007@gmail.com](mailto:zhouleo2007@gmail.com).
