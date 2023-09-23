"""Functions for printing results to the command line."""

from pint import Quantity
from ._parse import K_UNITS


def _get_dg0_str(dg0: Quantity) -> str:
    """Return the free energy of binding in kcal/mol."""
    return f"{dg0.to('kcal/mol').magnitude:#.3g} kcal/mol"


def _print_dg0(dg0: Quantity) -> None:
    """Print the free energy of binding in kcal/mol."""
    print(_get_dg0_str(dg0))


def _get_kd0_str(kd0: Quantity) -> str:
    """
    Return the dissociation constant with an appropriate prefix. Note that
    there is an implicit conversion from the standard dissociation constant to
    the dissociation constant.
    """
    # The appropriate prefix is the one that gives a value between 0.1 and 100
    # (i.e. between 1e-1 and 1e2)
    kd = kd0.magnitude
    for prefix, value in K_UNITS.items():
        if 1e-1 < kd / value <= 1e2:
            return f"{kd / value:#.3g} {prefix}"
    # The value is less than 0.1 pM or greater than 100 M
    if kd < 1e-10:
        return f"{kd / 1e-15:#.3g} fM"
    else:
        return f"{kd:#.3g} M"


def _print_kd0(kd0: Quantity) -> None:
    """
    Print the dissociation constant with an appropriate prefix. Note that there
    is an implicit conversion from the standard dissociation constant to the
    dissociation constant.
    """
    print(_get_kd0_str(kd0))
