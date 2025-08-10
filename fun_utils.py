import os

# Functions
def check_disk(command):
    print(os.system(command))    # Disk usage


def check_uptime(command):
    print(os.system(command))    # Load average

def check_date(command):
    print(os.system(command))    # Current date/time

def check_ram(command):
    print(os.system(command))    # RAM usage


# Function calls (must be outside any function)

check_uptime("uptime")    # Example command to check uptime
check_date("date")        # Example command to check date
check_ram("free -h")      # Example command to check RAM usage
check_disk("df -h")       # Example command to check disk usage






    
