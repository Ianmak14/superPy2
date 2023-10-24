# Import necessary module
from datetime import datetime

# Function to get date from a file based on the specified type


def getDateFromFile(type):

    # Read the date from the file and format it based on the specified type
    if type == "str":
        with open("./day/day.txt") as f:
            line = "".join(f.readline().split("-"))
            date = datetime.strptime(line, "%d%m%Y").date()
            formatted_date = datetime.strftime(date, "%d-%m-%Y")
        return formatted_date

    elif type == "date":
        with open("./day/day.txt") as f:
            line = "".join(f.readline().split("-"))
            date = datetime.strptime(line, "%d%m%Y").date()
        return date
