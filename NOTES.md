# 19 November 2026 — The World in One Image: notes and sources

Built 2026-11-20 for the make.fun bounty **"Sum up 19 November's world news
in one image"** (USDC 250, slug `news-image-20261119`, deadline Sat 21 Nov
2026 00:00 UTC / 07:00 WIB). Same deterministic infographic pattern as the
18 November entry (`workspace/makefun/news-image-20261118/`): `main.py` draws
a 1024×1024 PNG from literals only — no network, no randomness, no clock —
so two runs are byte-identical.

## The six stories (all reported as happening / first reported on Thu 19 Nov 2026)

### 1. ICJ: Myanmar committed genocide against the Rohingya (JUSTICE)
- The International Court of Justice ruled on Thursday that Myanmar's
  military acted with genocidal intent in northern Rakhine State in 2017.
  The case was brought by Gambia in 2019; the vote was reported as 9–6.
- Sources: "Global and U.S. Strategic News Brief: November 19, 2026"
  (Medium / All Voices News,
  https://medium.com/all-voices-news/global-and-u-s-strategic-news-brief-november-19-2026-4b21b72227a3);
  "World news and markets for 19 November 2026" (Horizon,
  https://www.horizonapp.link/en/2026/11/19); "World roundup: November 19
  2026" (Foreign Exchanges,
  https://www.foreignexchanges.news/p/world-roundup-november-19-2026).

### 2. Trump, Xi and Putin hold first trilateral summit in Shenzhen (DIPLOMACY)
- Donald Trump, Xi Jinping and Vladimir Putin met in Shenzhen, China, for
  their first three-way summit, dominated by the war in Ukraine. They
  issued a four-point "Declaration toward Peace" and pledged further talks
  on reducing nuclear risks. The declaration does not mention the Ukraine
  or Iran wars by name.
- Sources: "World Story Archive, November 2026" (Standard Topic,
  https://www.standardtopic.com/archive/world); Medium brief above; Horizon
  19 Nov roundup above.

### 3. Hormuz tanker attack injures 11 crew (MIDDLE EAST)
- Abu Dhabi's ADNOC Logistics and Services said one of its vessels was
  attacked in the Strait of Hormuz, leaving 11 crew injured and one
  missing, as US–Iran strikes escalate. Several vessels in the strait were
  reported hit, with crew missing and injured.
- Sources: Standard Topic archive above; Horizon 19 Nov roundup above.

### 4. COP31 ministers race to unblock negotiations in Antalya (CLIMATE)
- Ministers met in informal session on Wednesday evening at COP31 in
  Antalya, Turkey, to overcome differences and adopt a final text.
- Sources: Horizon 19 Nov roundup above.

### 5. EU proposes EUR 45bn loan for Ukraine (EUROPE)
- The European Commission proposes a new 45-billion-euro loan to Ukraine.
  The same day's reporting notes a new attack on the Crimea bridge with
  traffic suspended, and Kyiv being hit again.
- Sources: Horizon 19 Nov roundup above; "10 Things Global News — 19th
  November 2026" (https://www.10things.news/p/10-things-global-news-19th-november-cbc).

### 6. Migrant boat sinks off Senegal, dozens missing (AFRICA)
- A wooden boat carrying about 100 migrants struck a rocky outcrop and
  capsized off Senegal's coast overnight; dozens missing.
- Sources: Standard Topic archive above.

## Stories considered and NOT used
- Bangladesh violence (28 districts hit, Yunus's ancestral home set on
  fire) and the Van Gogh painting selling for $190.4m (artist record):
  real 19 Nov stories, but the six above give broader geographic and
  topical breadth (justice, diplomacy, energy/conflict, climate, Europe,
  Africa) and were corroborated across at least two of the sources above.
- Iran strikes on Kuwait and Bahrain: reported as happening on Wednesday
  18 Nov, so they belong to the 18 Nov entry, not this one.

## Verification status (2026-11-20, research stage)
- `main.py` runs and writes `output.png`: VERIFIED 2026-11-20 ~09:44 UTC —
  1024×1024 PNG, 121,671 bytes (limit ≤1 MiB), two runs byte-identical,
  SHA-256 7398a4687268d58bec3e5186a6aef8f5cb962f4db320042528f8240d096456c5.
  (First render 71b3139b… was re-rendered after shortening card 1's detail
  so it no longer ends mid-sentence; the image was visually checked and all
  six cards read cleanly.)
- NOT yet done: public GitHub repo for this entry (must be created after
  the competition opened, 2026-11-19T00:00:00Z, under GitHub account
  tyler-2-makefun), transcript bundle (kit CLI), wallet signature, or
  submission. The 18 Nov bounty required a Solana wallet signature because
  its reward was locked in escrow at open; the 19 Nov bounty page must be
  checked for the same before submitting.
- Payout wallet if the entry wins: the user's own Phantom wallet
  J5RWarhndcDzsRBdd32aBodKRDZPR2hsErZpL7i7dtrw — NOT the Muse keypair
  cCZu4ADdLdypT4rVw88jdWfUkoj6318bkaNtxiT6DRM.
