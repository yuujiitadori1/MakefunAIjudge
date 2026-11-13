"""ai-joke-03 entry (Python 3.13, standard library only).

Writes one original one-liner about AI coding agents to entry.txt.

The joke: an agent's confident "Done!" against the impossible reality
that the file it claims to have edited does not exist. Setup (the
declaration of completion) then twist (the work was on a file that was
never there) -- surprise, a truth every developer beside an agent
recognises, in two short sentences with no wasted words.

No network, no randomness, no time dependence: two runs write
byte-identical output. Reads $MAKEFUN_OUTPUT_DIR (else /output).
"""

import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"

JOKE = "My coding agent said 'Done!' The file it edited doesn't exist."

os.makedirs(OUTPUT_DIR, exist_ok=True)
with open(os.path.join(OUTPUT_DIR, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(JOKE)
