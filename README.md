# Hi, I'm Leo

I'm a CS student at Rice, originally from Auckland. I build full-stack software, especially workflow automation and applied AI. I enjoy talking with people about what they need, then turning that into useful software. I'm looking for a Summer 2027 software engineering internship.

Right now I'm building Kasheww at KEWW / Westchase Hospitality Group. It takes event work from client notes through proposals, kitchen preparation and invoicing. Reviewed PDF/text imports, equipment reservations and cost reporting join a Postgres client portal and Gmail/Calendar workflows in an invitation-only AWS beta. Gemini extracts facts for staff review; ordinary code handles pricing and permissions. A complete staff-operated event is still an acceptance step.

Alongside Kasheww, I built a LangGraph/FFmpeg video-review pilot with SQLite checkpoints and approval tied to the current version. I'm also experimenting with Postgres/pgvector retrieval for event emails.

With RiceApps, I'm co-developing Rice Football's analytics platform. My [Hudl IQ client](https://github.com/rice-apps/rice-football/pull/15) for games, rosters, plays and tracking is merged. My [PFF client](https://github.com/rice-apps/rice-football/pull/19), with JWT reuse and response validation, is in review. The team's work also includes CFBD access, Supabase-backed coaching Q&A, a report-library prototype and a fixture-backed R package.

At Rice, I'm working with Professor Jiarong Xing's group on external model-routing integrations for Claude Code and Codex through a Python/FastAPI proxy. I'm comparing OpenRouter and Not Diamond interfaces for model selection and tool-call compatibility. It's early integration work, with no measured routing results yet. My earlier contribution was fixing OAuth refresh, Keychain prompts and SSH usage tracking in TokenGate, a Swift macOS app.

Previously, I automated chip-test reporting at CanSemi with Python, Postgres, FastAPI and a React wafer map. At Inkstone, I worked on ABC Reads, an iOS reader with on-device OCR and a 113,000-entry offline dictionary.

## A few things I've built

### [BlunderNet](https://github.com/leozh0u/blundernet)

A free chess practice site at [blundernet.com](https://blundernet.com), with 3.25 million puzzles, a classroom mode, an engine I trained and Stockfish game review. Random puzzle selection went from 1.4 seconds to 0.9 ms using indexed shuffle keys and size-weighted cells. The backend uses Go, Postgres, Redis and SQS-fed ONNX workers, with Terraform for the AWS deployments. The [engine](https://github.com/leozh0u/blundernet-engine) has a C++ MCTS core alongside its PyTorch model.

### [Vestigo](https://github.com/leozh0u/vestigo)

Works out where a photograph was taken and shows the evidence behind its answer. A street-level answer needs street-level evidence. Its classifier uses frozen SigLIP features and was trained on 64,865 images split by location. It reached 142 km median error and 3.7% calibration error after temperature scaling. Those are classifier results, not end-to-end agent scores. The site at [vestigo.earth](https://vestigo.earth) plays recorded investigations; the agent and classifier can be demonstrated separately.

### [Perch](https://github.com/leozh0u/perch)

A floating macOS video player I built while practising on Zetamac. Paste a YouTube link, queue some videos and keep watching as you switch apps. Electron and JavaScript, with keyboard controls, global shortcuts and an optional second player.

### [Notch Apple](https://github.com/leozh0u/notch-apple)

My extension of [Boring Notch](https://github.com/TheBoredTeam/boring.notch). I added a native Spotify library browser, PKCE sign-in with Keychain token storage, playback targeted at this Mac, a focus dial and an upcoming-calendar view.

### [From Scratch](https://github.com/leozh0u/from-scratch)

Three of us built this crafting game at HackRice 16. Every recipe cites a source. Start with stone, wood and plant fibre, then work through the chains behind everyday objects. The graph runs offline in the browser; Gemini handles extra explanations. [Play it here](https://leozh0u.github.io/from-scratch/).

I started college in electrical engineering before switching to CS. Outside coding, I fence, play the drums, ski and play chess. More at [leozhou.fyi](https://leozhou.fyi), or reach me at [zhouleo2007@gmail.com](mailto:zhouleo2007@gmail.com).
