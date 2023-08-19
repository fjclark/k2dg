from k2dg import Q_
from k2dg._print import _print_dg0, _print_kd0


def test_print_dg0(capsys):
    _print_dg0(Q_(10, "kJ/mol"))
    captured = capsys.readouterr()
    assert captured.out == "2.39 kcal/mol\n"

    _print_dg0(Q_(-20, "kcal/mol"))
    captured = capsys.readouterr()
    assert captured.out == "-20.0 kcal/mol\n"


def test_print_kd0(capsys):
    _print_kd0(Q_(1e-6, "M"))
    captured = capsys.readouterr()
    assert captured.out == "1.00 uM\n"

    _print_kd0(Q_(1e-10, "M"))
    captured = capsys.readouterr()
    assert captured.out == "100. pM\n"

    _print_kd0(Q_(1e-2, "M"))
    captured = capsys.readouterr()
    assert captured.out == "10.0 mM\n"

    _print_kd0(Q_(1e4, "M"))
    captured = capsys.readouterr()
    assert captured.out == "1.00e+04 M\n"

    _print_kd0(Q_(1e-16, "M"))
    captured = capsys.readouterr()
    assert captured.out == "0.100 fM\n"
