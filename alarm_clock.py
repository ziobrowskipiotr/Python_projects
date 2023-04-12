from playsound import playsound
import time

Clear = "\033[2J"
Clear_and_return = "\033[H"
def alarm(seconds):
    time_elapsed = 0
    print(Clear)
    while time_elapsed < seconds:
        time.sleep(1)
        time_elapsed += 1

        time_left = seconds - time_elapsed
        minutes_lefts = time_left // 60
        seconds_left = time_left % 60

        print(f"{Clear_and_return}Alarm will sound {minutes_lefts:02d}:{seconds_left:02d}")
    playsound("alarm.mp3")

minutes = int(input("How many minutes to wait: "))
seconds = int(input("How many seconds to wait: "))
total_seconds = minutes * 60 + seconds
alarm(total_seconds)