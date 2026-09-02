# Sonnet Checker
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)

A small command-line tool and library that checks whether a poem matches the structural rules of a sonnet — Shakespearean, Petrarchan, or Spenserian — by verifying line count, rhyme scheme, and meter.

## What it checks

- Line count — the poem has exactly 14 lines.
- Rhyme scheme — line-ending words are looked up in the CMU Pronouncing Dictionary (via the `pronouncing` package) and grouped by rhyme sound.
- Meter — each line's syllables are counted and compared against 10 (iambic pentameter). Meter checking is a syllable-count verification only (it does not verify stress patterning).

## Quickstart (development)

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
# optional: install editable for development
pip install -e .
```

## Usage (CLI)

```bash
python app.py
```
The CLI runs interactively: choose a sonnet form and paste your poem, then press Enter twice to finish. The tool prints a pass/fail report.

## Programmatic usage

```python
from sonnet_checker.parser import parse_poem
from sonnet_checker.validators import validate_sonnet

text = open("my_sonnet.txt").read()
lines = parse_poem(text)
result = validate_sonnet(lines, "shakespearean")
print(result)  # dictionary with structure, rhyme, and meter results
```

## Short example
- Line count and meter pass, rhyme scheme can fail due to:
  - Pronunciation strictness (modern pronunciation vs historical eye-rhyme).
  - Unknown end words (archaic elisions not present in CMUdict).

See EXAMPLES.md for a full Sonnet 18 transcript and detailed example output.

## Running tests

```bash
python -m pytest
```

## Project layout

```
app.py                    CLI entry point
sonnet_checker/
  sonnet_types.py         Line count / rhyme scheme / meter rules per form
  parser.py               Splits raw poem text into lines
  structure.py            Line count check
  rhyme.py                Rhyme scheme check
  meter.py                Syllable-count meter check
  validators.py           Runs the checks and assembles the result
tests/                    pytest suite for each module
```

## How it works (concise)

- Rhyme matching: requires the rhyme sound from the last stressed vowel onward (CMUdict). Exact match is required by default.
- Unknown words: words missing from CMUdict are reported as "unknown" and cannot satisfy rhyme matches.
- Meter: checks syllable counts per line; for words missing from CMUdict the checker falls back to a vowel-group heuristic — this is inherently approximate.
- Rhyme and meter checks run only if line count passes.

## Known limitations

- Exact CMUdict rhyme matching will flag historical near-rhymes (eye rhymes) as failures.
- Archaic/elided spellings (e.g., `dimm'd`) may not be in CMUdict.
- Meter checking does not verify stress patterns (true scansion).

## Contributing

- Fork the repo, create a branch, run tests, and open a pull request.
- Suggested Dev workflow:
  - pip install -e .
  - run pytest and add tests for any change.
- If you’d like, I can add a CONTRIBUTING.md and issue templates in the PR.

## Roadmap (high level)

- Optional fuzzy rhyme matching for historical near-rhymes
- Normalizing archaic elided spellings before dictionary lookup
- Stress-pattern-aware meter checking
- Web interface or a small web UI on top of the same package

## License
This project is available under the MIT License. (I can add a LICENSE file to the branch and PR.)
