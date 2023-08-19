"""Tests for the parse module."""
from k2dg._parse import _parse_k_units, _parse_dg_units, _parse_temperature

import pytest

from k2dg import Q_


def test_parse_k_units():
    assert _parse_k_units("nM") == 1e-9
    assert _parse_k_units("M") == 1
    assert _parse_k_units("mM") == 1e-3
    assert _parse_k_units("uM") == 1e-6
    assert _parse_k_units("pM") == 1e-12
    with pytest.raises(ValueError) as e:
        _parse_k_units("foo")
    assert (
        str(e.value)
        == "Units foo not recognized. Please use one of dict_keys(['pM', 'nM', 'uM', 'mM', 'M'])."
    )


def test_parse_dg_units():
    assert _parse_dg_units("kcal/mol") == Q_(1, "kcal/mol")
    assert _parse_dg_units("kJ/mol") == Q_(1, "kJ/mol")
    with pytest.raises(ValueError):
        _parse_dg_units("foo")


def test_parse_temperature():
    assert _parse_temperature(273.15) == Q_(273.15, "K")
    assert _parse_temperature(300) == Q_(300, "K")
    with pytest.raises(ValueError):
        _parse_temperature(37)
