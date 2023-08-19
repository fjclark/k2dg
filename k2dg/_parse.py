"""Functions for parsing units from the command line input."""

from . import Q_

from pint import Quantity

K_UNITS = {"pM": 1e-12, "nM": 1e-9, "uM": 1e-6, "mM": 1e-3, "M": 1}
DG_UNITS = {"kcal/mol": Q_(1, "kcal/mol"), "kJ/mol": Q_(1, "kJ/mol")}


def _parse_k_units(units: str) -> float:
    """
    Parse a string of units (for the dissociation constant) into a float. Note
    that there is an implcit conversion from the dissociation constant to the
    standard dissociation constant.
    """
    lower_case_units = {k.lower(): v for k, v in K_UNITS.items()}
    try:
        return lower_case_units[units.lower()]
    except KeyError:
        raise ValueError(
            f"Units {units} not recognized. Please use one of {K_UNITS.keys()}."
        )


def _parse_dg_units(units: str) -> Quantity:
    """Parse a string of units (for the free energy of binding) into a float."""
    lower_case_units = {k.lower(): v for k, v in DG_UNITS.items()}
    try:
        return lower_case_units[units.lower()]
    except KeyError:
        raise ValueError(
            f"Units {units} not recognized. Please use one of {DG_UNITS.keys()}."
        )


def _parse_temperature(temperature: float) -> Quantity:
    """Parse a temperature in Kelvin."""
    if temperature < 100:
        raise ValueError(
            "Temperature must be in Kelvin. The supplied value is likely in Celsius."
        )
    return Q_(temperature, "K")
