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
