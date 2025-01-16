import time
import threading
import tkinter as tk
from tkinter import messagebox

def countdown_timer(seconds, label):
    while seconds >= 0:
        mins, secs = divmod(seconds, 60)
        time_format = '{:02d}:{:02d}'.format(mins, secs)
        label.config(text=time_format)
        time.sleep(1)
        seconds -= 1
    
    label.config(text="00:00")
    messagebox.showinfo("Time's up!", "The countdown has ended. 🎉")

def start_timer():
    try:
        user_input = int(entry.get())
        if user_input < 0:
            raise ValueError("Negative value")
        start_button.config(state='disabled')
        threading.Thread(target=countdown_timer, args=(user_input, timer_label)).start()
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter a positive integer.")

# Create main window
root = tk.Tk()
root.title("Countdown Timer")
root.geometry("400x300")  # Set the window size

# Create and place widgets with padding
entry = tk.Entry(root, font=("Helvetica", 16), width=10)
entry.pack(pady=20)

start_button = tk.Button(root, text="Start", command=start_timer, font=("Helvetica", 14), width=10)
start_button.pack(pady=10)

timer_label = tk.Label(root, text="00:00", font=("Helvetica", 48))
timer_label.pack(pady=20)

# Run the application
root.mainloop()
