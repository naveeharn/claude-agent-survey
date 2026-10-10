"""Greet someone by name."""

import sys

USAGE = "usage: python3 greeter/greet.py [-h] [--shout] NAME"
HELP = f"""{USAGE}

Print a greeting for NAME.

arguments:
  NAME        the name to greet (surrounding whitespace is ignored)

options:
  -h, --help  show this help message and exit
  --shout     print the greeting in uppercase

exit codes:
  0  greeting printed
  2  missing, extra or blank NAME, or unknown option"""


def greet(name: str, shout: bool = False) -> str:
    name = name.strip()
    if not name:
        raise ValueError("name must not be empty")
    greeting = f"Hello, {name}!"
    return greeting.upper() if shout else greeting


def main(argv: list[str]) -> int:
    if any(arg in ("-h", "--help") for arg in argv[1:]):
        print(HELP)
        return 0
    shout = "--shout" in argv[1:]
    args = [arg for arg in argv[1:] if arg != "--shout"]
    unknown = [arg for arg in args if arg.startswith("-")]
    if unknown:
        print(f"error: unknown option: {unknown[0]}", file=sys.stderr)
        print(USAGE, file=sys.stderr)
        return 2
    if len(args) != 1:
        print(USAGE, file=sys.stderr)
        return 2
    try:
        greeting = greet(args[0], shout=shout)
    except ValueError as e:
        print(f"error: {e}", file=sys.stderr)
        return 2
    print(greeting)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
