import re
import string

import pronouncing

_WORD_RE = re.compile(r"[A-Za-z']+")


def _last_word(line):
    words = _WORD_RE.findall(line)
    return words[-1] if words else None


def _rhyme_key(word):
    phones = pronouncing.phones_for_word(word.lower())
    if not phones:
        return None
    return pronouncing.rhyming_part(phones[0])


def _canonical_pattern(labels):
    mapping = {}
    canonical = []
    for label in labels:
        if label is None:
            canonical.append(None)
            continue
        if label not in mapping:
            mapping[label] = len(mapping)
        canonical.append(mapping[label])
    return canonical


def _labels_from_canonical(canonical):
    return [
        string.ascii_uppercase[index] if index is not None else "?"
        for index in canonical
    ]


def check_rhyme_scheme(lines, expected_scheme):
    """
    Check whether the end-rhymes of the poem match the expected rhyme scheme.

    :param lines: A list of strings representing the lines of the sonnet.
    :param expected_scheme: A list of letters (e.g. ["A", "B", "A", "B"])
        describing which lines are expected to rhyme with each other.
    :return: A dictionary containing the expected scheme, the detected
        rhyme groups per line, and whether the pattern matches. If a line's
        end word isn't found in the pronunciation dictionary, that line's
        rhyme key is None and the check cannot pass.
    """

    end_words = [_last_word(line) for line in lines]
    rhyme_keys = [_rhyme_key(word) if word else None for word in end_words]

    actual_pattern = _canonical_pattern(rhyme_keys)
    expected_pattern = _canonical_pattern(expected_scheme)

    passed = (
        len(lines) == len(expected_scheme)
        and None not in rhyme_keys
        and actual_pattern == expected_pattern
    )

    return {
        "expected": list(expected_scheme),
        "actual": _labels_from_canonical(actual_pattern),
        "end_words": end_words,
        "passed": passed,
    }
