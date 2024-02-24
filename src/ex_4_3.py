import os
from src.ex_4_0 import get_shutdown_events
from src.ex_4_2 import logstamp_to_datetime
from src.util import get_data_file_path

# Use this FILENAME variable to test your function.
FILENAME = get_data_file_path("messages.log")
# >>>> DO NOT MODIFY CODE ABOVE <<<<

def time_between_shutdowns(logfile):
    
    shutdown_events = get_shutdown_events(logfile)

    if len(shutdown_events) < 2:
        # Not enough shutdown events to compute time difference
        return None

    first_shutdown_time = logstamp_to_datetime(shutdown_events[0].split(' ')[1])
    last_shutdown_time = logstamp_to_datetime(shutdown_events[-1].split(' ')[1])

    time_difference = last_shutdown_time - first_shutdown_time
    return time_difference

# >>>> The code below will call your function and print the results
if __name__ == "__main__":
    print(f'{time_between_shutdowns(FILENAME)=}')
