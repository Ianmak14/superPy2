# Import necessary modules
from datetime import timedelta
from utils.getDateFromFile import getDateFromFile
from utils.utils import (
    checkInputDate,
    getAllItemsFromSoldCsvByDate,
    getAllItemsFromSoldCsvByDateArray,
    getRevenueFromSoldItemsList,
    returnDatesForWeekNumber,
    returnTableOfItems,
)
from rich.align import Align
from components.console import console, err_console

# Function to handle revenue requests


def handleRevenueRequest(input, date=None):

    if input == "today":
        # Get today's date
        day = getDateFromFile("str")

        # Get sold items for today
        soldItems = getAllItemsFromSoldCsvByDate(day)

        # Calculate total revenue
        totalRevenue = getRevenueFromSoldItemsList(soldItems)

        # Generate a table of sold items for display
        revenueTable = returnTableOfItems(soldItems, "revenue")

        # Set the date for the revenue report
        date = day

        # Format the revenue summary line
        revenueLine = f"Today's revenue so far: \u20ac {totalRevenue:.2f}"

    elif input == "yesterday":
        # Get yesterday's date
        day = getDateFromFile("date")
        day = day + timedelta(days=-1)
        day = day.strftime("%d-%m-%Y")

        # Get sold items for yesterday
        soldItems = getAllItemsFromSoldCsvByDate(day)

        # Calculate total revenue
        totalRevenue = getRevenueFromSoldItemsList(soldItems)

        # Generate a table of sold items for display
        revenueTable = returnTableOfItems(soldItems, "revenue")

        # Set the date for the revenue report
        date = day

        # Format the revenue summary line
        revenueLine = f"Yesterdays revenue: \u20ac {totalRevenue:.2f}"

    elif input == "date":
        # Check the input date format
        status = checkInputDate(date)

        # Handle different date types
        if status is None:
            err_console.print("Please enter a valid date")
            return

        if status["type"] == "week":
            # Get dates for the specified week
            dates = returnDatesForWeekNumber(int(date) - 1)

            # Get sold items for the week
            soldItems = getAllItemsFromSoldCsvByDateArray(dates)

            # Calculate total revenue
            totalRevenue = getRevenueFromSoldItemsList(soldItems)

            # Generate a table of sold items for display
            revenueTable = returnTableOfItems(soldItems, "revenue")

            # Format the revenue summary line
            revenueLine = f"[blue]{date}[/blue] revenue: \u20ac {totalRevenue:.2f}"

        else:
            # Get sold items for the specified date
            soldItems = getAllItemsFromSoldCsvByDate(date)

            # Calculate total revenue
            totalRevenue = getRevenueFromSoldItemsList(soldItems)

            # Generate a table of sold items for display
            revenueTable = returnTableOfItems(soldItems, "revenue")

            # Format the revenue summary line
            revenueLine = f"[blue]{date}[/blue] revenue: \u20ac {totalRevenue:.2f}"

    # Print the revenue report
    console.rule(f"[bold green]Revenue: {date}", style="red")
    console.print(Align.center(revenueTable))
    console.print(Align.center(revenueLine))
