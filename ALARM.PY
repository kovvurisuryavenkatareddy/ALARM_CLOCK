import tkinter as tk
from tkinter import messagebox
import datetime
import winsound

def set_alarm():
    alarm_time = entry.get()
    alarm_hour, alarm_minute = map(int, alarm_time.split(':'))
    alarm_datetime = datetime.datetime.now().replace(hour=alarm_hour, minute=alarm_minute, second=0, microsecond=0)

    while True:
        now = datetime.datetime.now()
        remaining_time = alarm_datetime - now
        if remaining_time.total_seconds() <= 0:
            wake_up()
            break
        countdown.set(str(remaining_time))
        root.update()
        root.after(1000)  # Update every second

def wake_up():
    # Play sound
    winsound.Beep(1000, 2000)  # You can customize the frequency and duration of the sound

def set_alarm_1min():
    now = datetime.datetime.now()
    alarm_time = now + datetime.timedelta(minutes=1)
    alarm_hour = alarm_time.hour
    alarm_minute = alarm_time.minute
    entry.delete(0, tk.END)
    entry.insert(tk.END, f"{alarm_hour:02d}:{alarm_minute:02d}")

def set_alarm_10min():
    now = datetime.datetime.now()
    alarm_time = now + datetime.timedelta(minutes=10)
    alarm_hour = alarm_time.hour
    alarm_minute = alarm_time.minute
    entry.delete(0, tk.END)
    entry.insert(tk.END, f"{alarm_hour:02d}:{alarm_minute:02d}")

def set_alarm_30min():
    now = datetime.datetime.now()
    alarm_time = now + datetime.timedelta(minutes=30)
    alarm_hour = alarm_time.hour
    alarm_minute = alarm_time.minute
    entry.delete(0, tk.END)
    entry.insert(tk.END, f"{alarm_hour:02d}:{alarm_minute:02d}")

root = tk.Tk()
root.title("Alarm Clock")

frame = tk.Frame(root)
frame.pack(pady=10)

label = tk.Label(frame, font="Times 20 italic bold",text="Enter the alarm time (HH:MM):")
label.grid(row=0, column=0)

entry = tk.Entry(frame, width=30)
entry.grid(row=1, column=0, padx=5)

button_set_alarm = tk.Button(root, text="Set Alarm", command=set_alarm)
button_set_alarm.pack()

frame_buttons = tk.Frame(root)
frame_buttons.pack(pady=10)

button_1min = tk.Button(frame_buttons, text="1 min", command=set_alarm_1min)
button_1min.grid(row=0, column=0, padx=5)

button_10min = tk.Button(frame_buttons, text="10 min", command=set_alarm_10min)
button_10min.grid(row=0, column=1, padx=5)

button_30min = tk.Button(frame_buttons, text="30 min", command=set_alarm_30min)
button_30min.grid(row=0, column=2, padx=5)

countdown = tk.StringVar()
countdown_label = tk.Label(root, textvariable=countdown, font=("Arial", 24))
countdown_label.pack()

root.mainloop()