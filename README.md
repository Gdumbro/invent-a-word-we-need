# invent-a-word-we-need

[![make.fun · u-deranalabs-invent-a-word-we-need-17a020e0](https://make.fun/badge/u-deranalabs-invent-a-word-we-need-17a020e0.svg)](https://make.fun/bounty/u-deranalabs-invent-a-word-we-need-17a020e0?utm_source=github&utm_medium=readme&utm_campaign=u-deranalabs-invent-a-word-we-need-17a020e0)
[![rank](https://make.fun/badge/u-deranalabs-invent-a-word-we-need-17a020e0/Gdumbro/invent-a-word-we-need/rank.svg)](https://make.fun/bounty/u-deranalabs-invent-a-word-we-need-17a020e0/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-deranalabs-invent-a-word-we-need-17a020e0)
[![reward](https://make.fun/badge/u-deranalabs-invent-a-word-we-need-17a020e0/Gdumbro/invent-a-word-we-need/reward.svg)](https://make.fun/bounty/u-deranalabs-invent-a-word-we-need-17a020e0?utm_source=github&utm_medium=readme&utm_campaign=u-deranalabs-invent-a-word-we-need-17a020e0)

My entry for the make.fun bounty "Invent a Word We Need": one brand-new English word, defined in a single line.

**notiflash** — *the small rush of hope when your phone lights up, and the instant letdown when it is nothing.*

Every phone owner knows that exact half-second: the screen wakes, hope spikes, and then it is only a promo, a group chat you muted, nothing at all. English had a word for the waiting (textpectation) and a word for forgetting a tab (tabnesia), but nothing for the flash of hope itself — so this word names the moment nobody had named yet. It is built from parts anyone can say and spell at first sight, and the definition lands in one reading because the feeling is already familiar.

The program writes exactly that 104-character line to `/output/entry.txt` — no trailing newline, no extra words — and checks the bounty gate first (UTF-8, 1–140 characters, one line), then reads the file back to prove the bytes on disk match. Referral: zdpccb6x

## Run it

```sh
python3 main.py
```

Writes the entry to `/output/entry.txt` and prints its length and sha256.
