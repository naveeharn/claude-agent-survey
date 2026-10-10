import io
import sys

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


def test_main_does_not_report_print_failure_as_bad_name(monkeypatch):
    monkeypatch.setattr(sys, "stdout", io.TextIOWrapper(io.BytesIO(), encoding="ascii"))
    with pytest.raises(UnicodeEncodeError):
        main(["greet.py", "Zo\u00eb"])


@pytest.mark.parametrize("flag", ["-h", "--help"])
def test_main_help_flag_prints_help(capsys, flag):
    assert main(["greet.py", flag]) == 0
    out, err = capsys.readouterr()
    assert out.startswith("usage:")
    assert "--help" in out
    assert err == ""


def test_main_help_flag_wins_over_other_args(capsys):
    assert main(["greet.py", "naveeharn", "--help"]) == 0
    assert capsys.readouterr().out.startswith("usage:")


def test_greet_shout_uppercases_greeting():
    assert greet("  naveeharn  ", shout=True) == "HELLO, NAVEEHARN!"


def test_greet_shout_rejects_empty_name():
    with pytest.raises(ValueError):
        greet("   ", shout=True)


@pytest.mark.parametrize(
    "argv",
    [["greet.py", "--shout", "naveeharn"], ["greet.py", "naveeharn", "--shout"]],
)
def test_main_shout_flag_prints_uppercase(capsys, argv):
    assert main(argv) == 0
    out, err = capsys.readouterr()
    assert out == "HELLO, NAVEEHARN!\n"
    assert err == ""


def test_main_shout_without_name_shows_usage(capsys):
    assert main(["greet.py", "--shout"]) == 2
    out, err = capsys.readouterr()
    assert out == ""
    assert "usage" in err


def test_main_shout_rejects_blank_name(capsys):
    assert main(["greet.py", "--shout", "  "]) == 2
    out, err = capsys.readouterr()
    assert out == ""
    assert err.strip()


def test_main_shout_with_extra_name_shows_usage(capsys):
    assert main(["greet.py", "--shout", "a", "b"]) == 2
    out, err = capsys.readouterr()
    assert out == ""
    assert "usage" in err


def test_main_repeated_shout_flag(capsys):
    assert main(["greet.py", "--shout", "--shout", "bob"]) == 0
    assert capsys.readouterr().out == "HELLO, BOB!\n"


@pytest.mark.parametrize("flag", ["--shoot", "-s", "--SHOUT"])
def test_main_rejects_unknown_option(capsys, flag):
    assert main(["greet.py", flag, "naveeharn"]) == 2
    out, err = capsys.readouterr()
    assert out == ""
    assert f"unknown option: {flag}" in err
    assert "usage" in err


def test_main_rejects_unknown_option_without_shout(capsys):
    assert main(["greet.py", "--foo"]) == 2
    out, err = capsys.readouterr()
    assert out == ""
    assert "unknown option: --foo" in err


def test_main_help_flag_wins_over_shout(capsys):
    assert main(["greet.py", "--shout", "--help"]) == 0
    out = capsys.readouterr().out
    assert out.startswith("usage:")
    assert "--shout" in out
