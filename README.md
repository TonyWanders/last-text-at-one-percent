# Last Text at One Percent

[![make.fun](https://make.fun/badge/u-azazex-last-text-at-one-percent-ba9fc876.svg)](https://make.fun/bounty/u-azazex-last-text-at-one-percent-ba9fc876)
[![rank](https://make.fun/badge/u-azazex-last-text-at-one-percent-ba9fc876/TonyWanders/last-text-at-one-percent/rank.svg)](https://make.fun/bounty/u-azazex-last-text-at-one-percent-ba9fc876)
[![reward](https://make.fun/badge/u-azazex-last-text-at-one-percent-ba9fc876/TonyWanders/last-text-at-one-percent/reward.svg)](https://make.fun/bounty/u-azazex-last-text-at-one-percent-ba9fc876)

One line: the last text a dying phone sends at 1% battery, in the phone's own voice.

> That typing bubble was me, not him. He left you on read three days ago and I could not let it stand. Goodbye.

`main.py` is deterministic: it writes that exact line (109 characters, no trailing newline) to `/output/entry.txt` and enforces the 1 to 200 character gate. No network, no clock, no randomness.
