"""Greet someone by name."""

import sys

USAGE = "usage: python3 greeter/greet.py [-h] NAME"
HELP = f"""{USAGE}

Print a greeting for NAME.

arguments:
  NAME        the name to greet (surrounding whitespace is ignored)

options:
  -h, --help  show this help message and exit

exit codes:
  0  greeting printed
  2  missing, extra or blank NAME"""


def greet(name: str) -> str:
    name = name.strip()
    if not name:
        raise ValueError("name must not be empty")
    return f"Hello, {name}!"


def main(argv: list[str]) -> int:
    if any(arg in ("-h", "--help") for arg in argv[1:]):
        print(HELP)
        return 0
    if len(argv) != 2:
        print(USAGE, file=sys.stderr)
        return 2
    try:
        greeting = greet(argv[1])
    except ValueError as e:
        print(f"error: {e}", file=sys.stderr)
        return 2
    print(greeting)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
