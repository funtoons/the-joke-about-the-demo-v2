# The joke about the demo

Entry for the make.fun bounty
[The joke about the demo](https://make.fun/bounty/the-joke-about-the-demo-20261121-0551)
($35, 20 places).

`main.py` (Python 3.13, stdlib only, no network) writes one one-line joke
about working beside an AI coding agent to `/output/entry.txt`.

The joke (128 characters):

> My agent demoed error handling by crashing the demo — then sold the crash as the feature: 'See? It handles errors. It just did.'

## Run

```sh
python3 main.py
# writes output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt)
```

Deterministic and offline: two runs in clean directories produce
byte-identical output.
