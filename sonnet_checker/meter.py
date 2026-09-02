import re

import pronouncing

_WORD_RE = re.compile(r"[A-Za-z']+")
_VOWEL_GROUPS_RE = re.compile(r"[aeiouy]+", re.IGNORECASE)

SYLLABLES_PER_LINE = 10  # iambic pentameter: five feet of two syllables each


def _estimate_syllables(word):
    """Rough fallback for words missing from the pronunciation dictionary."""

    groups = _VOWEL_GROUPS_RE.findall(word)
    return max(1, len(groups))


def _count_word_syllables(word):
    phones = pronouncing.phones_for_word(word.lower())
    if phones:
        return pronouncing.syllable_count(phones[0])
    return _estimate_syllables(word)


def _count_line_syllables(line):
    words = _WORD_RE.findall(line)
    return sum(_count_word_syllables(word) for word in words)


def check_meter(lines, expected_syllables=SYLLABLES_PER_LINE):
    """
    Check whether each line has the syllable count expected of the meter.

    This checks syllable count only, not stress pattern, so it confirms a
    line *could* be iambic pentameter without confirming the stresses
    actually fall unstressed-stressed.

    :param lines: A list of strings representing the lines of the sonnet.
    :param expected_syllables: Expected syllables per line (10 for
        iambic pentameter).
    :return: A dictionary with the per-line syllable counts and whether
        every line matches the expected count.
    """

    line_counts = [_count_line_syllables(line) for line in lines]
    passed = all(count == expected_syllables for count in line_counts)

    return {
        "expected": expected_syllables,
        "actual": line_counts,
        "passed": passed,
    }
