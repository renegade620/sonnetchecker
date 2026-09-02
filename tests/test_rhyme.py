from sonnet_checker.rhyme import check_rhyme_scheme

ABAB_MATCHING_LINES = [
    "I saw a cat",
    "beneath the sun",
    "it wore a hat",
    "and had some fun",
]

ABAB_MISMATCHED_LINES = [
    "I saw a cat",
    "beside the dog",
    "it wore a hat",
    "and had some fun",
]


def test_check_rhyme_scheme_passes_when_pattern_matches():
    result = check_rhyme_scheme(ABAB_MATCHING_LINES, ["A", "B", "A", "B"])

    assert result["passed"] is True
    assert result["actual"] == ["A", "B", "A", "B"]
    assert result["end_words"] == ["cat", "sun", "hat", "fun"]


def test_check_rhyme_scheme_fails_when_pattern_does_not_match():
    result = check_rhyme_scheme(ABAB_MISMATCHED_LINES, ["A", "B", "A", "B"])

    assert result["passed"] is False


def test_check_rhyme_scheme_fails_when_end_word_is_unrecognized():
    lines = ["a line ending in zzxxqqnotaword", "beneath the sun", "another zzxxqqnotaword", "and had some fun"]

    result = check_rhyme_scheme(lines, ["A", "B", "A", "B"])

    assert result["passed"] is False


def test_check_rhyme_scheme_ignores_punctuation_on_end_word():
    lines = ["I saw a cat,", "beneath the sun.", "it wore a hat;", "and had some fun!"]

    result = check_rhyme_scheme(lines, ["A", "B", "A", "B"])

    assert result["end_words"] == ["cat", "sun", "hat", "fun"]
    assert result["passed"] is True
