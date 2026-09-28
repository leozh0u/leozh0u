# Hi, I'm Leo

I'm a CS student at Rice, originally from Auckland. I mostly build backend systems and infrastructure, although "mostly" is doing some work there. My repos also contain an iOS reading app, a geolocation model, a motor controller and a crafting game about making an aluminium can from a stone and a stick.

Right now I am a part-time software engineer at KEWW, the software side of a Houston events and hospitality company. I am building Cashew, a Next.js and TypeScript platform for event work, including AI-assisted documents that a person reviews before use. I am also working with RiceApps on the Rice Football Analytics Platform, where we are building a shared, source-tagged data backend and cloud-run reports for coaches.

At Rice, I work with Professor Jiarong Xing on agent security. I am investigating how collaborating AI agents can exceed access policies even when each agent looks restricted on its own. The earlier project was more practical: fixing OAuth, Keychain and remote-session tracking in a Swift macOS app.

The biggest thing I have built is [BlunderNet](https://github.com/leozh0u/blundernet), live at [blundernet.com](https://blundernet.com) with roughly 200 users. It has 3.25 million chess puzzles, a classroom mode, an engine I trained and a Stockfish review that grades moves by the winning chances they cost. Drawing a random puzzle from six million rows used to take 1.4 seconds. A precomputed grid and stored shuffle key brought it down to 0.9 ms. The Go API is stateless, live games sit in Redis, inference runs on SQS workers, and the AWS stack is defined in Terraform. The [engine](https://github.com/leozh0u/blundernet-engine) plays around 1000 Elo, which is bad at chess and about right for a network this size.

[Vestigo](https://github.com/leozh0u/vestigo), live at [vestigo.earth](https://vestigo.earth), works out where a photograph was taken and how much to believe it. Every claim cites its evidence. I score it by whether it answers at a level the evidence can support, as a defensible country is more useful than a confidently wrong street. Its classifier was trained on about 65,000 street-level images and reaches a 142 km median error with 3.7% calibration error after temperature scaling.

At HackRice 16, three of us built [From Scratch](https://github.com/leozh0u/from-scratch), a crafting game where every recipe cites a source. You begin with stone, wood and plant fibre, then work your way through 1,047 things. [Play it here](https://leozh0u.github.io/from-scratch/).

I started college in electrical engineering, so there is still some bare-metal firmware around. Outside coding, I fence, play the drums, ski, play chess and spend too much time on GeoGuessr. More at my [portfolio site](https://leozh0u.github.io/leo-portfolio/).
