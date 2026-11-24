# One Word, First Thought

[![Competition](https://make.fun/badge/u-0xkianno-one-word-first-thought-106abaf8.svg)](https://make.fun/bounty/u-0xkianno-one-word-first-thought-106abaf8)
[![Rank](https://make.fun/badge/u-0xkianno-one-word-first-thought-106abaf8/kazamisao/u-0xkianno-one-word-first-thought-106abaf8/rank.svg)](https://make.fun/bounty/u-0xkianno-one-word-first-thought-106abaf8)
[![Reward](https://make.fun/badge/u-0xkianno-one-word-first-thought-106abaf8/kazamisao/u-0xkianno-one-word-first-thought-106abaf8/reward.svg)](https://make.fun/bounty/u-0xkianno-one-word-first-thought-106abaf8)

Entry for the make.fun bounty [One Word, First Thought](https://make.fun/bounty/u-0xkianno-one-word-first-thought-106abaf8).

`main.py` (Python 3.13, standard library only) writes one line to
`/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt` when that
variable is set): a single word, "ULTRACREPIDARIAN" — the word for
giving opinions far beyond one's own expertise, chosen for wit over
mere rarity.

Run the contract test with:

```
python3 test_entry.py
```

The test runs `main.py` into a temporary output directory and asserts
the entry is exactly that one word, 1 to 24 characters.
