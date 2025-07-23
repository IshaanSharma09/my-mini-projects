import time
import datetime
import pygame

def set_alarm(alarm_time):
    try:
        datetime.datetime.strptime(alarm_time, "%H:%M:%S")
    except ValueError:
        print("Invalid⚠️⚠️  time format. Please use HH:MM:SS.")
        exit()
    print(f"Alarm ⏳ set for {alarm_time}")
    isrunning = True
    alarm = "Alram_clock/bs_alert.mp3"
    while isrunning:
        time_now = datetime.datetime.now().strftime("%H:%M:%S")
        print(time_now)
        if alarm_time == time_now:
            print("TIME UP🚨🚨!!")

            pygame.mixer.init()
            pygame.mixer.music.load(alarm)
            pygame.mixer.music.play(-1)

            while True:
                choice = input("Enter 'stop' to stop ❌ or 'snooze' to snooze 😴 for 5 minutes: ").strip().lower()
                if choice == 'stop':
                    pygame.mixer.music.stop()
                    return  
                elif choice == 'snooze':
                    pygame.mixer.music.stop()
                    snooze_time = datetime.datetime.now() + datetime.timedelta(minutes=5)
                    alarm_time = snooze_time.strftime("%H:%M:%S")
                    print(f"Snoozed 🔄! Next alarm at {alarm_time}")
                    break
                else:
                    print("Invalid 	⚠️⚠️ input. Please enter 'stop' or 'snooze'.")

            isrunning = False

        time.sleep(1)
if __name__ == "__main__":
    alarm_time = input("Enter the time ⏰ ('H:M:S') : ").strip()
    set_alarm(alarm_time)