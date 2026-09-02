# Sonnet Checker

A command-line tool that checks whether a poem matches the structural rules
of a sonnet: Shakespearean, Petrarchan, or Spenserian.

## Status

Three checks run today, in order, once line count passes:

- **Line count** — must match the form (14 lines for all three supported forms).
- **Rhyme scheme** — end words are looked up in the CMU Pronouncing
  Dictionary (via the `pronouncing` package) and grouped by rhyme; the
  resulting pattern is compared to the form's expected scheme. A word
  missing from the dictionary (e.g. "dimm'd") can't be matched and fails
  the check rather than being guessed.
- **Meter** — syllables per line are counted and compared to 10 (iambic
  pentameter). This checks syllable *count* only, not stress pattern, so it
  doesn't yet confirm the syllables actually fall unstressed/stressed.

See the roadmap below for what's still missing.

## Install

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Usage

```bash
python app.py
```

You'll be asked to pick a sonnet form (Shakespearean, Petrarchan, or
Spenserian) and then paste your poem, finishing with a blank line. The tool
prints the validation result.

## Run tests

```bash
python -m pytest
```

## Roadmap

- [ ] Stress-pattern (true iambic) meter checking, beyond syllable count
- [ ] Web UI on top of the same `sonnet_checker` package
