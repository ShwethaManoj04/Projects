import time
import threadpoolctl
from tkinter import Tk, Label, Button
from plyer import notification
class PomodoroTimer:
    def __init__(self, root):
        self.root = root
        self.root.title("Pomodoro Timer")

        self.timer_running = False
        self.paused = False
        self.work_duration = 1500  # 25 minutes
        self.break_duration = 600  # 10 minutes
        self.current_time = self.work_duration
        self.count = 0

        self.label = Label(root, text="Ready to start your Pomodoro!", font=("Helvetica", 14))
        self.label.pack(pady=10)

        self.time_label = Label(root, text=self.format_time(self.current_time), font=("Helvetica", 48))
        self.time_label.pack(pady=10)

        self.start_button = Button(root, text="Start", command=self.start_timer, width=10)
        self.start_button.pack(side="left", padx=5)

        self.pause_button = Button(root, text="Pause", command=self.pause_timer, width=10)
        self.pause_button.pack(side="left", padx=5)

        self.stop_button = Button(root, text="Stop", command=self.stop_timer, width=10)
        self.stop_button.pack(side="left", padx=5)

    def format_time(self, seconds):
        minutes = seconds // 60
        seconds = seconds % 60
        return f"{minutes:02}:{seconds:02}"

    def update_timer(self):
        if self.timer_running and not self.paused:
            self.current_time -= 1
            if self.current_time <= 0:
                self.timer_ended()
            self.time_label.config(text=self.format_time(self.current_time))
            self.root.after(1000, self.update_timer)

    def start_timer(self):
        if not self.timer_running:
            self.timer_running = True
            self.paused = False
            self.update_timer()

    def pause_timer(self):
        self.paused = not self.paused
        if not self.paused:
            self.update_timer()

    def stop_timer(self):
        self.timer_running = False
        self.current_time = self.work_duration
        self.time_label.config(text=self.format_time(self.current_time))
        self.label.config(text="Timer stopped. Ready to start again!")

    def timer_ended(self):
        self.timer_running = False
        self.count += 1
        notification.notify(
            title="Good work!",
            message=f"Take a 10-minute break! You have completed {self.count} Pomodoros so far.",
        )
        self.current_time = self.break_duration
        self.time_label.config(text=self.format_time(self.current_time))
        self.label.config(text="Break time! Press 'Start' to begin your break.")
        self.root.after(1000, self.start_break)

    def start_break(self):
        self.timer_running = True
        self.update_timer()

if __name__ == "__main__":
    root = Tk()
    timer = PomodoroTimer(root)
    root.mainloop()





