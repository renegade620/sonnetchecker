from sonnet_checker.sonnet_types import SONNET_TYPES
from sonnet_checker.structure import check_line_count

def validate_sonnet(lines, sonnet_type):
    """
    Validates the sonnet based on the specified sonnet type.

    :param lines: A list of strings representing the lines of the sonnet.
    :param sonnet_type: The type of sonnet (e.g., "shakespearean", "petrarchan", "spenserian").
    :return: A dictionary containing validation results.
    """

    rules = SONNET_TYPES.get(sonnet_type)
    if rules is None:
        raise ValueError(f"Unknown sonnet type: {sonnet_type!r}")

    line_result = check_line_count(lines, rules["line_count"])

    return {
        "sonnet_type": sonnet_type,
        "structure": line_result,
    }