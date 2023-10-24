# Import necessary modules
from argparse import Namespace
from components.inputParser import create_parser
import sys

# Add the component path to sys.path
sys.path.insert(0, "./components")

# Test case for buy command


def test_input():
    # Create a parser
    parser = create_parser()

    # Parse the arguments
    parsing = parser.parse_args

    # Assert that the parsing result matches the expected Namespace
    assert parsing(["buy", "-n", "Orange", "-p", "2"]) == Namespace(
        buy=True, name="Orange", price=2, amount=1, expiration=10
    )

# Test case for sell command


def test_input2():
    # Create a parser
    parser = create_parser()

    # Parse the arguments
    parsing = parser.parse_args

    # Assert that the parsing result matches the expected Namespace
    assert parsing(["sell", "-n", "Broccoli", "-p", "3"]) == Namespace(
        sell=True, name="Broccoli", price=3, amount=1
    )
