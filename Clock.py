import time

def focus_timer(minutes):
    seconds = minutes * 60
    start_time = time.time()
    end_time = start_time + seconds

    while time.time() < end_time:
        remaining_time = int(end_time - time.time())
        minutes_remaining = remaining_time // 60
        seconds_remaining = remaining_time % 60
        print(f"Remaining time: {minutes_remaining:02d}:{seconds_remaining:02d}", end="\r")
        time.sleep(1)

    print("Time is up! Stay focused!")

focus_duration = int(input("Enter focus duration in minutes: "))
focus_timer(focus_duration)
