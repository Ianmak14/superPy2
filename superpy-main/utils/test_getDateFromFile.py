# Import necessary modules
import datetime
from getDateFromFile import getDateFromFile

# Define the test function


def test_getDateFromFile():

    # Call the function to get the result
    result = getDateFromFile()

    # Assert that the result is an instance of the datetime.date class
    assert isinstance(result, datetime.date)
