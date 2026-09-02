# Examples

This file contains the full interactive transcript used as an example in the README (Sonnet 18 checked as Shakespearean). Use it for reference or testing.

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

Notes on the example
- "temperate" vs "date" is an eye rhyme: modern pronunciation does not rhyme them, so the checker reports that.
- Archaic elided forms (`dimm'd`, `untrimm'd`, `ow'st`, `grow'st`) are not in CMUdict and are reported as unknown; unknown words cannot be matched for rhyme.
