from sonnet_checker.meter import check_meter

TEN_SYLLABLE_LINE = "The light of dawn breaks soft upon the day"
SHORT_LINE = "The cat sat"


def test_check_meter_passes_for_ten_syllable_lines():
    result = check_meter([TEN_SYLLABLE_LINE, TEN_SYLLABLE_LINE])

    assert result["passed"] is True
    assert result["actual"] == [10, 10]


def test_check_meter_fails_for_short_lines():
    result = check_meter([SHORT_LINE])

    assert result["passed"] is False
    assert result["actual"][0] < 10


def test_check_meter_uses_fallback_for_unknown_words():
    result = check_meter(["zzz bzzt"])

    assert result["actual"] == [2]
    assert result["passed"] is False


def test_check_meter_accepts_lines_needing_an_alternate_pronunciation():
    # "temperate" is 9 syllables under its primary CMUdict pronunciation but
    # 10 under its alternate ("tem-per-ate" vs. "tem-p'rate") - the line is
    # genuinely iambic pentameter and should pass.
    line = "Thou art more lovely and more temperate:"

    result = check_meter([line])

    assert result["passed"] is True
