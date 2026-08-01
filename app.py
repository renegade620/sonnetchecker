from sonnet_checker.parser import parse_poem
from sonnet_checker.validators import validate_sonnet

SONNET_CHOICES = {
    "1": "shakespearean",
    "2": "petrarchan",
    "3": "spenserian",
}

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

print("Paste your sonnet (blank line to finish):")
poem_lines = []
while True:
    line = input()
    if not line.strip():
        break
    poem_lines.append(line)
poem = "\n".join(poem_lines)

lines = parse_poem(poem)
result = validate_sonnet(lines, sonnet_type)
print(result)