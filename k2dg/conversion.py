"""Functions to convert between standard dissociation constants and free energies of binding."""

import numpy as np
from pint import Quantity
from scipy import constants

from . import ureg

__all__ = ["get_kbT", "kd0_to_dg0", "dg0_to_kd0"]


@ureg.check("[temperature]")
def get_kbT(temperature: Quantity) -> Quantity:
    """Return the value of k_b * T at a given temperature."""
    k = constants.k * ureg.J / ureg.K
    na = constants.N_A / ureg.mol
    return k * temperature * na


# @ureg.check("[None]", "[temperature]")  # None is not accepted TODO: Find a work around
def kd0_to_dg0(kd0: float, temperature: Quantity) -> Quantity:
    """Convert an standard dissociation constant a standard free energy of binding."""
    return -get_kbT(temperature) * np.log(1 / kd0)


@ureg.check("[energy] / [substance]", "[temperature]")
def dg0_to_kd0(dg0: Quantity, temperature: Quantity) -> float:
    """Convert a standard free energy of binding to a standard dissociation constant."""
    return 1 / np.exp(-dg0 / get_kbT(temperature))
