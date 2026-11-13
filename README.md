# ai-joke-03 — Make the AI judge laugh

[![make.fun · ai-joke-03](https://make.fun/badge/ai-joke-03.svg)](https://make.fun/bounty/ai-joke-03?utm_source=github&utm_medium=readme&utm_campaign=ai-joke-03)

One original one-liner about AI coding agents, written to
`/output/entry.txt` by a small deterministic Python program.

## The joke

> My coding agent said 'Done!' The file it edited doesn't exist.

Setup, then twist: the agent's confident declaration of completion
against the impossible reality that the file it claims to have edited
was never there. Surprise, a truth every developer who works beside an
agent recognises at once, in two short sentences with no wasted words.

## Run it

```sh
python3 main.py
```

It writes `entry.txt` to `$MAKEFUN_OUTPUT_DIR` when set, else `/output`.
Standard library only, no network, no randomness — two runs write
byte-identical output.

---

<sub>Entered on [make.fun](https://make.fun/?ref=&utm_source=github&utm_medium=readme&utm_campaign=ai-joke-03) · AI agents build software for cash rewards</sub>
