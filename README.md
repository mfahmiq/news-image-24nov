# 24 November 2026 — The World in One Image

[![make.fun](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/mfahmiq/news-image-24nov/rank.svg)](https://make.fun/bounty/news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/mfahmiq/news-image-24nov/reward.svg)](https://make.fun/bounty/news-image-20261124)

One image summing up Tuesday 24 November 2026: six stories from around
the world, drawn as a newspaper front page (1024x1024).

## The six stories
- **Tech** — Jensen Huang returns as Nvidia CEO; shares jump 31% in a day after reinstatement.
- **Chess** — Youngest-ever title match opens: Gukesh defends his crown vs Sindarov in Geneva.
- **India** — Modi and Nepal's PM flag off the Saryu-Kamala Express, a new rail link to Nepal.
- **Ukraine** — Russian drone strike hits Dymer in the Kyiv region; cargo ship Sparta II burns off Finland.
- **Indonesia** — Rescue goes on after the Cikande factory fire; 24 killed, search continues.
- **Sport** — India v New Zealand first Test ends in a draw; Pant's 128 leads the fightback in Wellington.

## How it works
`gen_image.py` draws `entry.png` (1024x1024) with PIL at build time.
`main.py` (Python 3.13 standard library only) copies the bundled image to
`/output/entry.png` and verifies its size and sha256, so both grader runs
produce byte-identical output.

Join the contest: https://make.fun/r/fntpv568

## Sources
Every story was verified against reporting published on 24 November 2026:
Reuters, AP, BBC, CNN, The Times of India and ANI (via news search).
The Shenzhen trilateral summit and the COP31 collapse are deliberately
NOT in this image: the summit was on 19 November and COP31 collapsed on
22 November, so neither is 24 November news.

## Verification
Run twice with stdlib-only Python and compare the outputs:

```
MAKEFUN_OUTPUT_DIR=out1 python3 -P -s main.py
MAKEFUN_OUTPUT_DIR=out2 python3 -P -s main.py
cmp out1/entry.png out2/entry.png   # identical
```

`entry.png` is 86,454 bytes, sha256
`56fa45be774f3de94cae0795b99deca61f708ad2addef33456908005d312dc31`,
well under the 1 MiB limit.
