from io import StringIO
from unittest.mock import patch
from k2dg._cli import run_cli  # Replace 'your_module' with the actual module name


def test_run_cli():
    # Test case 1: Convert from kd to dg
    test_args = ["2dg", "1.0", "uM", "-t", "298.15"]

    with patch("sys.argv", ["k2dg"] + test_args):
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            run_cli()

    # Validate the behavior of the function for this test case
    output = mock_stdout.getvalue()
    assert "-8.19 kcal/mol\n" in output

    # Test case 2: Convert from dg to kd
    test_args = ["2kd", "-20.0", "kJ/mol", "-t", "310.15"]

    with patch("sys.argv", ["k2dg"] + test_args):
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            run_cli()

    # Validate the behavior of the function for this test case
    output = mock_stdout.getvalue()
    assert "0.428 mM\n" in output

    # Test case 3: Missing subcommand
    test_args = []

    with patch("argparse.ArgumentParser.print_help") as mock_print_help:
        with patch("sys.argv", ["k2dg"] + test_args):
            run_cli()

    # Ensure that argparse.ArgumentParser.print_help was called
    mock_print_help.assert_called_once()
