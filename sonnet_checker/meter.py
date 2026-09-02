import re

import pronouncing

_WORD_RE = re.compile(r"[A-Za-z']+")
_VOWEL_GROUPS_RE = re.compile(r"[aeiouy]+", re.IGNORECASE)

SYLLABLES_PER_LINE = 10  # iambic pentameter: five feet of two syllables each


def _estimate_syllables(word):
    """Rough fallback for words missing from the pronunciation dictionary."""

    groups = _VOWEL_GROUPS_RE.findall(word)
    return max(1, len(groups))


def _syllable_options(word):
    """All syllable counts CMUdict lists for this word (e.g. elided vs. full)."""

    phones_list = pronouncing.phones_for_word(word.lower())
    if phones_list:
        return sorted({pronouncing.syllable_count(phones) for phones in phones_list})
    return [_estimate_syllables(word)]


def _count_word_syllables(word):
    """The word's primary (first-listed) pronunciation, for display."""

    return _syllable_options(word)[0]


def _count_line_syllables(line):
    words = _WORD_RE.findall(line)
    return sum(_count_word_syllables(word) for word in words)


def _line_can_reach(line, expected_syllables):
    """Whether some combination of the line's valid pronunciations sums to
    the expected count. Poets rely on this: "every" can scan as 2 or 3
    syllables, "temperate" as 2 or 3, etc., and a line is metrical if any
    valid reading fits."""

    words = _WORD_RE.findall(line)
    possible_totals = {0}
    for word in words:
        options = _syllable_options(word)
        possible_totals = {total + option for total in possible_totals for option in options}
    return expected_syllables in possible_totals


def check_meter(lines, expected_syllables=SYLLABLES_PER_LINE):
    """
    Check whether each line can be read with the syllable count expected of
    the meter.

    This checks syllable count only, not stress pattern, so it confirms a
    line *could* be iambic pentameter without confirming the stresses
    actually fall unstressed-stressed. A line passes if any of its words'
    valid dictionary pronunciations sum to the expected count, since poets
    routinely rely on alternate readings (e.g. "ev'ry" vs. "every") to hit
    the meter.

    :param lines: A list of strings representing the lines of the sonnet.
    :param expected_syllables: Expected syllables per line (10 for
        iambic pentameter).
    :return: A dictionary with each line's syllable count (using each
        word's primary pronunciation) and whether every line can reach the
        expected count under some valid pronunciation.
    """

    line_counts = [_count_line_syllables(line) for line in lines]
    passed = all(_line_can_reach(line, expected_syllables) for line in lines)

    return {
        "expected": expected_syllables,
        "actual": line_counts,
        "passed": passed,
    }
