# Sonnet Checker

A command-line tool that checks whether a poem matches the structural rules
of a sonnet — Shakespearean, Petrarchan, or Spenserian — checking line
count, rhyme scheme, and meter.

## What it checks

| Check | What it verifies |
| --- | --- |
| **Line count** | The poem has exactly 14 lines. |
| **Rhyme scheme** | Each line's end word is looked up in the CMU Pronouncing Dictionary (via the [`pronouncing`](https://pypi.org/project/pronouncing/) package) and grouped by rhyme sound; the resulting pattern is compared against the chosen form's expected scheme (e.g. `ABAB CDCD EFEF GG` for Shakespearean). |
| **Meter** | Each line's syllables are counted and checked against 10 (iambic pentameter). A line passes if *any* of its words' valid dictionary pronunciations reach 10 — poets routinely rely on alternate readings (e.g. "ev'ry" vs. "every") to hit the meter, so the checker allows for that. |

Rhyme and meter are only checked once line count passes.

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

You'll be asked to pick a sonnet form, then paste your poem — press **Enter
twice** when you're done. The tool prints a pass/fail report.

## Example

Checking Shakespeare's Sonnet 18 against the Shakespearean form:

```
$ python app.py
Welcome to the Sonnet Checker!

Please choose a sonnet type:
1. Shakespearean
2. Petrarchan
3. Spenserian
Enter your choice (1, 2, or 3): 1
Paste your sonnet, then press Enter twice to finish:
Shall I compare thee to a summer's day?
Thou art more lovely and more temperate:
Rough winds do shake the darling buds of May,
And summer's lease hath all too short a date;
Sometime too hot the eye of heaven shines,
And often is his gold complexion dimm'd;
And every fair from fair sometime declines,
By chance, or nature's changing course, untrimm'd;
But thy eternal summer shall not fade,
Nor lose possession of that fair thou ow'st,
Nor shall death brag thou wander'st in his shade,
When in eternal lines to time thou grow'st:
So long as men can breathe, or eyes can see,
So long lives this, and this gives life to thee.


Sonnet type: Shakespearean

Line count [PASS]
  14 / 14 lines

Rhyme scheme [FAIL]
  expected: A B A B C D C D E F E F G G
  detected: A B A C D ? D ? E ? E ? F F
  end words: day, temperate, May, date, shines, dimm'd, declines, untrimm'd, fade, ow'st, shade, grow'st, see, thee

Meter [PASS] (10 syllables/line, iambic pentameter)
  line  1: 10 syllables
  line  2: 9 syllables
  line  3: 10 syllables
  line  4: 10 syllables
  line  5: 10 syllables
  line  6: 10 syllables
  line  7: 10 syllables
  line  8: 10 syllables
  line  9: 10 syllables
  line 10: 10 syllables
  line 11: 10 syllables
  line 12: 10 syllables
  line 13: 10 syllables
  line 14: 10 syllables

Overall: FAIL
```

Line count and meter pass, but rhyme scheme fails — which is worth reading
closely, because it shows the two ways rhyme checking can come up short:

**Pronunciation strictness.** Position 2 (`temperate`, expected to rhyme
with position 4, `date`) is assigned a different letter (`B` vs. `C`)
because the two words genuinely don't share an ending sound in modern
pronunciation:

```
temperate -> ends in "-er-ət" / "-r-ət"  (EH1 M P (ER0) AH0 T)
date      -> ends in "-eɪt"              (EY1 T)
```

This isn't a bug — it's Sonnet 18's well-known **eye rhyme**: "temperate"
and "date" look like they might rhyme and may have scanned closer in Early
Modern English, but they don't rhyme by modern pronunciation, and the
checker reports that accurately rather than forcing a match. Rhyme checking
here is strict: it requires the full rhyming sound (from the last stressed
vowel onward) to match exactly, so historical near-rhymes and eye rhymes
will register as failures.

**Elided spellings.** `dimm'd`, `untrimm'd`, `ow'st`, and `grow'st` all show
up as `?` in the detected pattern. These archaic contracted forms simply
aren't entries in the CMU Pronouncing Dictionary, so there's no
pronunciation data to check them against — the checker reports "unknown"
rather than guessing, and an unknown end word can never satisfy a rhyme
match.

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

## Known limitations

- Rhyme matching requires the CMUdict rhyming sound to match exactly;
  historical near-rhymes and eye rhymes (like "temperate"/"date" above)
  will fail even when a poet intended them to rhyme.
- A word missing from CMUdict — most commonly an archaic elided spelling —
  can't be rhyme-checked at all and is reported as unknown.
- Syllable counting falls back to a rough vowel-group estimate for words
  missing from CMUdict, rather than a real pronunciation.
- Meter checking verifies syllable count only; it does not verify that
  stress actually falls unstressed/stressed (true iambic scansion).

## Roadmap

- Optional fuzzy rhyme matching (vowel-sound only, ignoring the coda) for
  historical near-rhymes
- Normalizing archaic elided spellings (`dimm'd` → `dimmed`, `ow'st` →
  `owest`) before dictionary lookup
- Stress-pattern-aware meter checking
- A web interface on top of the same `sonnet_checker` package
