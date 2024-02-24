try:
    from src.util import get_data_file_path
except ImportError:
    from util import get_data_file_path

# Use this FILENAME variable to test your function.
FILENAME = get_data_file_path('messages.log')
# >>>> DO NOT MODIFY CODE ABOVE <<<<

def get_shutdown_events(logfile):
    """
    Reads a log file and returns a list of lines where a shutdown was initiated.

    Args:
    - logfile (str): The path to the log file.

    Returns:
    - list: A list of lines where a shutdown was initiated. If no shutdown events are found, an empty list is returned.
    """
    shutdown_events = []

    with open(logfile, 'r') as file:
        for line in file:
            if "Shutdown initiated" in line:
                shutdown_events.append(line.strip())

    return shutdown_events

# >>>> The code below will call your function and print the results
if __name__ == "__main__":
    print(f"{get_shutdown_events(FILENAME)=}")
