from sonnet_checker.structure import check_line_count


def test_check_line_count_passes_when_counts_match():
    lines = [f"line {i}" for i in range(14)]

    result = check_line_count(lines, 14)

    assert result == {"expected": 14, "actual": 14, "passed": True}


def test_check_line_count_fails_when_too_few():
    lines = [f"line {i}" for i in range(10)]

    result = check_line_count(lines, 14)

    assert result == {"expected": 14, "actual": 10, "passed": False}


def test_check_line_count_fails_when_too_many():
    lines = [f"line {i}" for i in range(20)]

    result = check_line_count(lines, 14)

    assert result == {"expected": 14, "actual": 20, "passed": False}


def test_check_line_count_handles_empty_list():
    result = check_line_count([], 14)

    assert result == {"expected": 14, "actual": 0, "passed": False}
