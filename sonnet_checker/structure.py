def check_line_count(lines, expected_line_count):
    """
    Check if the sonnet has the expected number of lines.

    :param lines: A list of strings representing the lines of the sonnet.
    :param expected_line_count: The expected number of lines in the sonnet.
    :return: A dictionary containing the expected line count, actual line count, and a boolean indicating if the check passed.
    """

    actual_line_count = len(lines)

    return {
        "expected": expected_line_count,
        "actual": actual_line_count,
        "passed": actual_line_count == expected_line_count
    }