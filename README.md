# Sonnet Checker

A command-line tool that checks whether a poem matches the structural rules
of a sonnet: Shakespearean, Petrarchan, or Spenserian.

## Status

Only line count is currently validated (a sonnet must have 14 lines). Rhyme
scheme and meter are defined per form in `sonnet_checker/sonnet_types.py` but
are not yet checked — see the roadmap below.

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

- [ ] Rhyme scheme validation against each form's expected pattern
- [ ] Meter validation (iambic pentameter)
- [ ] Web UI on top of the same `sonnet_checker` package
