"""Greet someone by name."""

import sys


def greet(name: str) -> str:
    name = name.strip()
    if not name:
        raise ValueError("name must not be empty")
    return f"Hello, {name}!"


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("usage: python3 greeter/greet.py NAME", file=sys.stderr)
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
