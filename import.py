# import_os.py
import os
import datetime


def run_command(command):
    return os.system(command)

def show_date():      # Function to show the current date
    return datetime.datetime.today()

    
today = show_date()     # Call the function to get today's date
print(today)  # Print the date


          






