import time

def digital_clock():
    """Displays the current time in HH:MM:SS format."""
    try:
        while True:
            # Format time as HH:MM:SS
            current_time = time.strftime("%H:%M:%S")
            # \r overwrites the current line; end="" prevents starting a new line
            print(f"\rCurrent Time: {current_time}", end="", flush=True)
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nClock stopped.")

if __name__ == "__main__":
    digital_clock()