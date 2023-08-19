"""Command line interface for k2dg."""

import argparse
from . import ureg, Q_
from .conversion import dg0_to_kd0 as _dg0_to_kd0, kd0_to_dg0 as _kd0_to_dg0
from ._parse import (
    _parse_dg_units,
    _parse_k_units,
    _parse_temperature,
    K_UNITS,
    DG_UNITS,
)
from ._print import _print_dg0, _print_kd0


def run_cli() -> None:
    """Run the command line interface."""

    global_parser = argparse.ArgumentParser(prog="k2dg")
    global_parser.add_argument(
        "-v", "--version", action="version", version="%(prog)s 0.1.1"
    )
    subparsers = global_parser.add_subparsers(
        title="subcommands",
        help="Converters from dissociation constants to free energies of binding and vice versa.",
    )

    # Add subparsers to handle conversion in each direction
    to_dg_parser = subparsers.add_parser(
        "2dg", help="Convert a dissociation constant to a free energy of binding."
    )
    to_kd_parser = subparsers.add_parser(
        "2kd", help="Convert a free energy of binding to a dissociation constant."
    )

    subparser_dict = {
        to_dg_parser: {
            "units": K_UNITS,
            "value": "kd",
            "func": _kd0_to_dg0,
            "parse_func": _parse_k_units,
            "print_func": _print_dg0,
        },
        to_kd_parser: {
            "units": DG_UNITS,
            "value": "dg",
            "func": _dg0_to_kd0,
            "parse_func": _parse_dg_units,
            "print_func": _print_kd0,
        },
    }

    for subparser in subparser_dict:
        subparser.add_argument(
            "value",
            type=float,
            help=f"The value of {subparser_dict[subparser]['value']}.",
        )
        subparser.add_argument(
            "units",
            type=str,
            help=f"The units of the value. Must be one of {list(subparser_dict[subparser]['units'].keys())}.",
        )
        subparser.add_argument(
            "-t",
            "--temperature",
            type=float,
            help="The temperature (in Kelvin) at which the dissociation constant was measured.",
            default=298.15,
        )
        subparser.set_defaults(func=subparser_dict[subparser]["func"])
        subparser.set_defaults(parse_func=subparser_dict[subparser]["parse_func"])
        subparser.set_defaults(print_func=subparser_dict[subparser]["print_func"])

    args = global_parser.parse_args()
    # Check that a subparser was selected
    if not hasattr(args, "func"):
        global_parser.print_help()
        return
    units = args.parse_func(args.units)
    temperature = _parse_temperature(args.temperature)
    args.print_func(args.func(args.value * units, temperature))
