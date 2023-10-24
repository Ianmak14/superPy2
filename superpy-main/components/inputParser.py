import argparse


def create_parser():
    # Create the main argument parser
    parser = argparse.ArgumentParser(
        prog="SuperPy",
        usage="SuperPy [buy | sell | report | advance]",
        description="Welcome to your favorite local grocery store",
        epilog="Please use the above help to work with our program",
    )

    # Create subparsers for different actions
    instruction = parser.add_subparsers(
        metavar="Subcommands",
        title="SuperPy",
        help="Use [subcommand] -h to get extra info on usage of each subcommand",
    )

    # Buy command
    buy = instruction.add_parser(
        "buy",
        help="Basic action type for buying an item.",
    )
    buy.add_argument("buy", action="store_true", default=False)
    buy.add_argument("--name", "-n", metavar="PRODUCT",
                     help="Supply product name for the product to buy", required=True)
    buy.add_argument("--price", "-p", metavar="PRICE", type=float,
                     help="Supply the price of the product", required=True)
    buy.add_argument("--amount", "-a", metavar="[AMOUNT]", default=1,
                     help="Supply the amount of products purchased (default=1)")
    buy.add_argument("--expiration", "-e", metavar="[EXPIRATION]", type=int, default=10,
                     help="Supply the amount in days of the shelf life of a product (default=10)")

    # Sell command
    sell = instruction.add_parser(
        "sell",
        help="Basic action type for selling an item.",
    )
    sell.add_argument("sell", action="store_true", default=False)
    sell.add_argument("--name", "-n", metavar="NAME",
                      help="Supply product name for the product to sell", required=True)
    sell.add_argument("--price", "-p", metavar="PRICE", type=float,
                      help="Supply the price of the product", required=True)
    sell.add_argument("--amount", "-a", metavar="[AMOUNT]", default=1,
                      help="Supply the amount of products sold (default=1)")

    # Advance command
    advance = instruction.add_parser(
        "advance",
        help="Advance day by X days (default=1)",
    )
    advance.add_argument("advance", action="store_true", default=False)
    advance.add_argument("-d", metavar="DAYS", type=int,
                         default=1, help="Advance day by X days (default=1)")

    # Report command
    report = instruction.add_parser(
        "report",
        help="Produce several reports",
    )
    report.add_argument("report", action="store_true", default=False)

    # Subcommands for reports
    report_subcommands = report.add_subparsers(
        metavar="Subcommands",
        title="Report",
        help="Use [subcommand] -h to get extra info on usage of each subcommand",
    )

    # Inventory report
    inventory = report_subcommands.add_parser(
        "inventory", help="Show current inventory")
    inventory.add_argument("inventory", action="store_true", default=False)

    # Revenue report
    revenue = report_subcommands.add_parser(
        "revenue", help="Show revenue for different time periods")
    revenue.add_argument("revenue", action="store_true", default=False)
    revenue.add_argument("--today", action="store_true",
                         default=False, help="Returns revenue for today.")
    revenue.add_argument("--yesterday", action="store_true",
                         default=False, help="Returns revenue for yesterday.")
    revenue.add_argument(
        "--date", "-d", help="Specify a certain date or period.")

    # Profit report
    profit = report_subcommands.add_parser(
        "profit", help="Show profit for different time periods")
    profit.add_argument("profit", action="store_true", default=False)
    profit.add_argument("--today", action="store_true",
                        default=False, help="Returns profit for today.")
    profit.add_argument("--yesterday", action="store_true",
                        default=False, help="Returns profit for yesterday.")
    profit.add_argument(
        "--date", "-d", help="Specify a certain date or period.")

    # Reset command
    reset = instruction.add_parser("reset", help="Reset database")
    reset.add_argument("reset", nargs="?", default=True)

    # Demo command
    demo = instruction.add_parser("demo", help="Load dummy data to experiment")
    demo.add_argument("demo", nargs="?", default=True)

    return parser
