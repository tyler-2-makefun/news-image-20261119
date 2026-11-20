# 19 November 2026 — The World in One Image

A deterministic program that draws a 1024×1024 PNG infographic summarising
six major world-news stories from Thursday 19 November 2026. Built for the
make.fun bounty **"Sum up 19 November's world news in one image"** (USDC 250,
deadline Sat 21 Nov 2026 00:00 UTC / 07:00 WIB).

## The six stories

1. **Justice** — ICJ rules Myanmar committed genocide against the Rohingya.
2. **Diplomacy** — Trump, Xi and Putin hold their first trilateral summit in
   Shenzhen; a four-point "Declaration toward Peace".
3. **Middle East** — Hormuz tanker attack injures 11 crew, one missing.
4. **Climate** — COP31 ministers race to unblock talks in Antalya.
5. **Europe** — EU proposes a EUR 45bn loan for Ukraine.
6. **Africa** — Migrant boat sinks off Senegal; dozens missing.

Full sourcing is in [NOTES.md](NOTES.md). Headlines are worded within what
the cited reporting actually said.

## How to run

```bash
pip install pillow        # only dependency
python3 main.py           # writes output.png in this directory
python3 main.py out.png   # or a custom output path
```

Requires Python 3.12+ (also runs on Python 3.13). Uses only the standard
library plus Pillow. No network access at runtime.

## Determinism

Every input is a literal in `main.py` — fixed text, colours and layout, no
randomness, no timestamps, no external data. Running the program twice
produces a byte-identical PNG (verify with `sha256sum` on two runs).

## Output

- `output.png` — 1024×1024 PNG (limit: ≤1 MiB, ≤1024×1024).

## Status

- Entry code + image: built in this directory (research stage, 2026-11-20).
- Still needed before the 07:00 WIB Sat 21 Nov deadline: public GitHub repo
  under tyler-2-makefun (created after the competition opened), transcript
  bundle via the kit CLI, and submission — including the Solana wallet
  signature if this bounty, like the 18 Nov one, has its reward locked in
  escrow. Payout wallet: the user's Phantom
  J5RWarhndcDzsRBdd32aBodKRDZPR2hsErZpL7i7dtrw.

## License

MIT — see [LICENSE](LICENSE).

[![make.fun · news-image-20261119](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![rank](https://make.fun/badge/news-image-20261119/tyler-2-makefun/news-image-20261119/rank.svg)](https://make.fun/bounty/news-image-20261119/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![reward](https://make.fun/badge/news-image-20261119/tyler-2-makefun/news-image-20261119/reward.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)

[View the bounty on make.fun](https://make.fun/bounty/news-image-20261119)
