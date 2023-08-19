"""Test the conversion functions."""

import numpy as np
from k2dg import conversion
from k2dg import Q_


def test_get_kbT():
    temperature = Q_(298.15, "K")
    expected_kbT = Q_(0.592483, "kcal/mol")
    assert np.isclose(
        conversion.get_kbT(temperature).to("kcal/mol").magnitude,
        expected_kbT.magnitude,
        rtol=1e-5,
    )


def test_kd0_to_dg0():
    temperature = Q_(298.15, "K")
    kd0 = 0.347e-6
    expected_dg0 = Q_(-8.812586, "kcal/mol")
    print(conversion.kd0_to_dg0(kd0, temperature).to("kcal/mol").magnitude)
    assert np.isclose(
        conversion.kd0_to_dg0(kd0, temperature).to("kcal/mol").magnitude,
        expected_dg0.magnitude,
        rtol=1e-3,
    )


def test_dg0_to_kd0():
    temperature = Q_(298.15, "K")
    dg0 = Q_(-8.812586, "kcal/mol")
    expected_kd0 = 0.347e-6
    print(conversion.dg0_to_kd0(dg0, temperature))
    assert np.isclose(
        conversion.dg0_to_kd0(dg0, temperature),
        expected_kd0,
        rtol=1e-3,
    )
