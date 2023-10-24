# Import necessary modules
from functools import reduce
import sys
from components.console import console, err_console
from utils.getDateFromFile import getDateFromFile
from utils.utils import (
    adjustLineInInventoryCsv,
    getAllItemsByNameFromInventoryCsv,
    removeLineFromInventoryCsv,
    appendRowToSoldCsv,
)

# Add the CSV path to sys.path
sys.path.insert(0, "../csv")

# Function to handle the selling of products


def handleSell(inputObj):
    # Extract relevant information from the input object
    name = inputObj.name.lower()
    price = inputObj.price
    amount = int(inputObj.amount)
    sold = 0

    # Get the current day from the file to set the sell date
    day = getDateFromFile("str")

    # Get the inventory items with the specified product name
    inStock = getAllItemsByNameFromInventoryCsv(name)

    # Check the total amount of the product in stock
    inStockAmount = reduce(
        lambda x, y: x + y, [d["amount"] for d in inStock], 0)

    # Loop that handles the selling of the products until the order is fulfilled or the stock runs out
    while amount > 0:
        if inStock:
            for stock in inStock:
                # The amount is higher than what is in stock
                if amount > stock["amount"] and inStockAmount != 0:
                    if amount == stock["amount"]:
                        console.print("[blue bold]OK")
                    amount -= stock["amount"]
                    inStockAmount -= stock["amount"]
                    sold += stock["amount"]
                    # Remove the line from the inventory.csv and write it into sell.csv
                    appendRowToSoldCsv(
                        stock["id"], name, stock["amount"], day, price)
                    removeLineFromInventoryCsv(int(stock["id"]))
                    continue
                elif inStockAmount == 0:
                    err_console.print(f"You were only able to sell {sold}")
                    amount = 0
                    break
                else:
                    appendRowToSoldCsv(stock["id"], name, amount, day, price)
                    if amount == stock["amount"]:
                        removeLineFromInventoryCsv(int(stock["id"]))
                    else:
                        adjustLineInInventoryCsv(int(stock["id"]), amount)
                    # Set amount to 0 to reset the loop as the sale has been fulfilled
                    amount = 0
                    sold += amount
                    console.print("[blue bold]OK")
                    break
        else:
            err_console.print("ERROR: Product not in stock.")
            break
