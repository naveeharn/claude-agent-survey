import pytest

from greet import greet, main


def test_greet_returns_greeting():
    assert greet("naveeharn") == "Hello, naveeharn!"


def test_greet_strips_whitespace():
    assert greet("  naveeharn  ") == "Hello, naveeharn!"


def test_greet_rejects_empty_name():
    with pytest.raises(ValueError):
        greet("   ")


def test_main_prints_greeting(capsys):
    assert main(["greet.py", "naveeharn"]) == 0
    assert capsys.readouterr().out == "Hello, naveeharn!\n"


def test_main_without_name_shows_usage(capsys):
    assert main(["greet.py"]) == 2
    assert "usage" in capsys.readouterr().err


def test_main_rejects_blank_name(capsys):
    assert main(["greet.py", "  "]) == 2
    assert capsys.readouterr().err.strip()
