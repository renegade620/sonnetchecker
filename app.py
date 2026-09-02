from sonnet_checker.parser import parse_poem
from sonnet_checker.validators import validate_sonnet

SONNET_CHOICES = {
    "1": "shakespearean",
    "2": "petrarchan",
    "3": "spenserian",
}


def _status(passed):
    return "PASS" if passed else "FAIL"


def format_result(result):
    structure = result["structure"]
    checks_passed = [structure["passed"]]

    report = [
        f"Sonnet type: {result['sonnet_type'].capitalize()}",
        "",
        f"Line count [{_status(structure['passed'])}]",
        f"  {structure['actual']} / {structure['expected']} lines",
    ]

    if "rhyme" in result:
        rhyme = result["rhyme"]
        checks_passed.append(rhyme["passed"])
        report += [
            "",
            f"Rhyme scheme [{_status(rhyme['passed'])}]",
            f"  expected: {' '.join(rhyme['expected'])}",
            f"  detected: {' '.join(rhyme['actual'])}",
            f"  end words: {', '.join(rhyme['end_words'])}",
        ]

    if "meter" in result:
        meter = result["meter"]
        checks_passed.append(meter["passed"])
        report += [
            "",
            f"Meter [{_status(meter['passed'])}] ({meter['expected']} syllables/line, iambic pentameter)",
        ]
        for line_no, count in enumerate(meter["actual"], start=1):
            report.append(f"  line {line_no:>2}: {count} syllables")

    report += ["", f"Overall: {_status(all(checks_passed))}"]
    return "\n".join(report)

print("Welcome to the Sonnet Checker!")
print()
print("Please choose a sonnet type:")
print("1. Shakespearean")
print("2. Petrarchan")
print("3. Spenserian")

choice = input("Enter your choice (1, 2, or 3): ")
sonnet_type = SONNET_CHOICES.get(choice)
if sonnet_type is None:
    raise SystemExit(f"Invalid choice: {choice!r}. Expected 1, 2, or 3.")

print("Paste your sonnet, then press Enter twice to finish:")
poem_lines = []
blank_streak = 0
while True:
    try:
        line = input()
    except EOFError:
        break
    if not line.strip():
        blank_streak += 1
        if blank_streak >= 2:
            break
        continue
    blank_streak = 0
    poem_lines.append(line)
poem = "\n".join(poem_lines)

lines = parse_poem(poem)
result = validate_sonnet(lines, sonnet_type)
print()
print(format_result(result))