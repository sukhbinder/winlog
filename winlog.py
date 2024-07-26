import ctypes
from datetime import datetime
import os
import sched
import time
import argparse

event_schedule = sched.scheduler(time.time, time.sleep)

user32 = ctypes.windll.user32

def get_active_window_title_str():
    length = user32.GetWindowTextLengthW(user32.GetForegroundWindow())
    buffer_size = length + 2 * len(" ")
    title_buffer = ctypes.create_unicode_buffer(buffer_size)

    if length > 0:
        user32.GetWindowTextW(user32.GetForegroundWindow(), title_buffer, buffer_size)

    return title_buffer.value

USER_PATH = os.path.expanduser("~/Desktop")
os.makedirs(USER_PATH, exist_ok=True)


# every 30 seconds
TIME_INTERVAL = 30


def get_current_time():
    now = datetime.now()
    month = now.strftime("%m").upper()  # Get month as uppercase abbreviation (APR)
    day = now.strftime("%d")  # Get day as zero-padded string (09)
    year = now.strftime("%Y")  # Get year (2024)
    hour = now.strftime("%H")  # Get hour in 24-hour format (10)
    minute = now.strftime("%M")  # Get minute as zero-padded string (25)
    seconds = now.strftime("%S")  # get seconds as zero-padded string

    # Check for AM/PM
    meridian = "AM" if now.hour < 12 else "PM"

    ctime = f"{year}-{month}-{day} {hour}:{minute}:{seconds}"
    return ctime


def log_win_title():
    log_file = os.path.join(USER_PATH, "log.txt")
    wintitle = get_active_window_title_str()
    datestr = get_current_time()
    with open(log_file, "a", encoding='utf-8') as fin:
         fin.write(datestr+","+wintitle+"\n")
    event_schedule.enter(TIME_INTERVAL, 1, log_win_title, ())

    

def main():
    parser = argparse.ArgumentParser(description="Write Windows Title to Desktop Log")
    _ = parser.parse_args()
    print("Winlog Initiated.")
    event_schedule.enter(10, 1, log_win_title, ())
    event_schedule.run()


if __name__ == "__main__":
    main()

