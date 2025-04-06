import tkinter as tk
from tkinter import messagebox
import time

def start_countdown():
    try:
        time_left = int(entry.get())
        countdown(time_left)
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number")

def countdown(time_left):
    if time_left > 0:
        label.config(text=f"Time left: {time_left} sec")
        root.after(1000, countdown, time_left - 1)
    else:
        label.config(text="Time's up!")
        messagebox.showinfo("Countdown Finished", "Time's up!")

# Create the main window
root = tk.Tk()
root.title("Countdown Timer")
root.geometry("300x200")

# Create widgets
entry = tk.Entry(root, font=("Arial", 14))
entry.pack(pady=10)

start_button = tk.Button(root, text="Start Countdown", command=start_countdown)
start_button.pack(pady=5)

label = tk.Label(root, text="Enter time in seconds", font=("Arial", 14))
label.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
