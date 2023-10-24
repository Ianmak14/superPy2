# Import necessary modules
from datetime import timedelta
from utils.getDateFromFile import getDateFromFile
from components.console import console, err_console

# Function to advance the internal date of the program


def advance(days):
    # Get the current day from the file
    current_day = getDateFromFile("date")

    try:
        # Calculate the new day by adding the specified number of days
        new_day = current_day + timedelta(days=days)

        # Format the new day for display
        formatted_day = new_day.strftime("%d-%m-%Y")

        # Update the current day in the file
        with open("./day/day.txt", "w") as file:
            file.write(formatted_day)

        # Print a success message
        console.print(f"[green]Current day set to: {formatted_day}")
        console.print("[blue bold]OK")

    except Exception as e:
        # Print an error message if there is a failure
        err_console.print("Failure!")
        err_console.print(f"Error: {e}")
