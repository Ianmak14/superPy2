# Import necessary modules
from datetime import timedelta
from utils.getDateFromFile import getDateFromFile
from utils.utils import (
    checkInputDate,
    getAllItemsFromSoldCsvByDate,
    getAllItemsFromSoldCsvByDateArray,
    getProfitFromSoldItemsList,
    returnDatesForWeekNumber,
    returnTableOfItems,
)
from rich.align import Align
from components.console import console

# Function to handle profit requests


def handleProfitRequest(input, date=None):

    if input == "today":
        # Get today's date
        day = getDateFromFile("str")

        # Get sold items for today
        soldItems = getAllItemsFromSoldCsvByDate(day)

        # Calculate total profit
        totalProfit = getProfitFromSoldItemsList(soldItems)

        # Generate a table of sold items for display
        profitTable = returnTableOfItems(soldItems, "profit")

        # Set the date for the profit report
        date = day

        # Format the profit summary line
        profitLine = f"Today's profit so far: \u20ac {totalProfit:.2f}"

    elif input == "yesterday":
        # Get yesterday's date
        day = getDateFromFile("date")
        day = day + timedelta(days=-1)
        day = day.strftime("%d-%m-%Y")

        # Get sold items for yesterday
        soldItems = getAllItemsFromSoldCsvByDate(day)

        # Calculate total profit
        totalProfit = getProfitFromSoldItemsList(soldItems)

        # Generate a table of sold items for display
        profitTable = returnTableOfItems(soldItems, "profit")

        # Set the date for the profit report
        date = day

        # Format the profit summary line
        profitLine = f"Yesterdays profit: \u20ac {totalProfit:.2f}"

    elif input == "date":
        # Check the input date format
        status = checkInputDate(date)

        # Handle different date types
        if status["status"]:
            if status["type"] == "week":
                # Get dates for the specified week
                dates = returnDatesForWeekNumber(int(date) - 1)

                # Get sold items for the week
                soldItems = getAllItemsFromSoldCsvByDateArray(dates)

                # Calculate total profit
                totalProfit = getProfitFromSoldItemsList(soldItems)

                # Generate a table of sold items for display
                profitTable = returnTableOfItems(soldItems, "profit")

                # Format the profit summary line
                profitLine = f"[blue]{date}[/blue] profit: \u20ac {totalProfit:.2f}"
            else:
                # Get sold items for the specified date
                soldItems = getAllItemsFromSoldCsvByDate(date)

                # Calculate total profit
                totalProfit = getProfitFromSoldItemsList(soldItems)

                # Generate a table of sold items for display
                profitTable = returnTableOfItems(soldItems, "profit")

                # Format the profit summary line
                profitLine = f"[blue]{date}[/blue] profit: \u20ac {totalProfit:.2f}"

    # Print the profit report
    console.rule(f"[bold green]Profit: {date}", style="red")
    console.print(Align.center(profitTable))
    console.print(Align.center(profitLine))
