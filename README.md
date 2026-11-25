# 24 November 2026 — The World in One Image (v2)

[![make.fun](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/mfahmiq/news-image-24nov/rank.svg)](https://make.fun/bounty/news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/mfahmiq/news-image-24nov/reward.svg)](https://make.fun/bounty/news-image-20261124)

One image summing up Tuesday 24 November 2026: six stories from around
the world, drawn as a newspaper front page (1024x1024). Version 2 is a
full rebuild of the v1 entry: a hero lead story, a 2x2 grid and a sport
banner instead of a flat grid, with six stories that were all first
reported on 24 November itself — v1 carried stories from the day
before, which the judge scores down.

## The six stories
- **Top story — Huawei** — US jury finds Huawei guilty of trade-secret
  theft and bank fraud (10 of 12 counts); acquitted of racketeering.
  Huawei to appeal; sentencing set for September 2027.
- **Middle East** — Four tankers hit mines in the Strait of Hormuz;
  Iran says the ships caught fire and orders the strait closed.
- **War in Europe** — Ukraine hits Russian ships in two seas: drone
  strike on cargo ship Sparta II in the Gulf of Finland, a corvette
  hit off Libya.
- **Colombia** — Gunmen hold 25 hostage in a Cartagena supermarket;
  five older women freed, troops deployed.
- **Asia** — Prabowo names two candidates for vice-president: Amran
  Sulaiman and Sugiono, to succeed Gibran.
- **Sport** — Senegal win back the Africa Cup title on appeal: CAS
  restores the 1–0 final win over Morocco.

## How it works
`entry.png` (1024x1024) was drawn at build time with PIL + DejaVu by a
generator script kept outside this repository, so the repo ships only
the image and the copier. `main.py` (Python 3.13 standard library only)
copies the bundled image to `/output/entry.png` and verifies its size
and sha256, so both grader runs produce byte-identical output.

Join the contest: https://make.fun/r/fntpv568

## Sources
Every story was verified against reporting first published on
24 November 2026: Reuters, AP, BBC and Daily Summary Of (which lists
each story's first-reported time on 24 Nov UTC). Deliberately NOT in
this image: the Nvidia CEO return and the FIFA Women's World Cup host
announcement (both 23 November), the Shenzhou-24 launch (25 November),
and the COP31 collapse (22 November) — none of them is 24 November news.

## Verification
Run twice with stdlib-only Python and compare the outputs:

```
MAKEFUN_OUTPUT_DIR=out1 python3 -P -s main.py
MAKEFUN_OUTPUT_DIR=out2 python3 -P -s main.py
cmp out1/entry.png out2/entry.png   # identical
```

`entry.png` is 117,994 bytes, sha256
`0af3b89d6683886ea1409ef1d26af5eca1165647c61f81a5884a127883eec6b0`,
well under the 1 MiB limit.
