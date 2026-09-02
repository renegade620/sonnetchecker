import pytest

from sonnet_checker.validators import validate_sonnet

VALID_SONNET_LINES = [f"line {i}" for i in range(14)]


@pytest.mark.parametrize(
    "sonnet_type", ["shakespearean", "petrarchan", "spenserian"]
)
def test_validate_sonnet_returns_structure_for_known_types(sonnet_type):
    result = validate_sonnet(VALID_SONNET_LINES, sonnet_type)

    assert result["sonnet_type"] == sonnet_type
    assert result["structure"] == {"expected": 14, "actual": 14, "passed": True}


def test_validate_sonnet_flags_wrong_line_count():
    result = validate_sonnet(VALID_SONNET_LINES[:10], "shakespearean")

    assert result["structure"]["passed"] is False
    assert result["structure"]["actual"] == 10


def test_validate_sonnet_raises_for_unknown_type():
    with pytest.raises(ValueError, match="Unknown sonnet type"):
        validate_sonnet(VALID_SONNET_LINES, "limerick")
