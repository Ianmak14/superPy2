# Import necessary modules
import csv
from components.console import console
from utils.getDateFromFile import getDateFromFile
from rich.table import Table
from rich.align import Align

from utils.utils import getItemFromBoughtCsvById

# Function to display the current inventory


def displayCurrentInventory():
    # Get the current day
    day = getDateFromFile("str")

    # Create a table for displaying inventory
    table = Table(min_width=100)

    with open("./csv/inventory.csv") as inv:
        lines = csv.reader(inv)
        count = 0

        for line in lines:
            # Add column headers only once
            if count == 0:
                table.add_column("Product Name", style="magenta", no_wrap=True)
                table.add_column("Amount", justify="center",
                                 style="blue", no_wrap=True)
                table.add_column("Price", justify="right",
                                 style="green", no_wrap=True)
                table.add_column(
                    "Expiration", justify="center", style="yellow", no_wrap=True
                )
                count += 1
            else:
                # Get additional item details from the bought csv
                item = getItemFromBoughtCsvById(int(line[0]))

                # Add a row to the table with item information
                table.add_row(
                    line[1], line[2], "\u20ac " +
                    item["price"], item["expiration"]
                )

    # Print the inventory report
    console.rule(f"[bold green]Inventory: {day}", style="red")
    console.print(Align.center(table))
