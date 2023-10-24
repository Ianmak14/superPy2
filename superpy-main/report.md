# SuperPy Report

## 1. Argparse Efficiency

The implementation of argument parsing in SuperPy leverages the simplicity and effectiveness of Argparse.
Utilizing the following code snippet:
instruction = parser.add_subparsers(
metavar="Subcommands",
)

Subcommands are defined, allowing for comprehensive input checks. This design streamlines the parsing process and facilitates the implementation of program flow logic in `main.py`. The approach of using:

buy.add_argument("buy", action="store_true", default=False)

Ensures that the program recognizes the 'buy' command with no need for additional parameters:
python main.py buy

The `parsed` object's attributes are then examined in `main.py` to determine the specific command invoked:
if hasattr(parsed, "buy"):
handleBuy(parsed)

## 2. DRY Principle Adherence

SuperPy adheres to the Don't Repeat Yourself (DRY) principle, enhancing code maintainability and facilitating future refactoring. An illustrative example is the **`getDateFromFile()`** function, housed in `utils.py`. This function uniformly retrieves the current date from a designated .txt file, essential for maintaining the program's internal clock.

def getDateFromFile(type): # Implementation details...

The flexibility of this function enables its seamless integration throughout the program, providing either a `_Date` object or a formatted `str` representing the current date.

## 3. Structural Coherence

SuperPy's overall program structure, though open to optimization, exhibits a clarity that aids comprehension. The code is organized with an emphasis on readability, where files are kept concise for ease of perusal. A deliberate effort has been made to segregate business logic and presentation, resulting in the use of descriptive, albeit lengthy, function names. This approach prioritizes clarity over brevity, ensuring that the focus remains on the logical flow of the program rather than intricate implementation details.
