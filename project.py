import tkinter as tk

# Function to handle button click events
def button_click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(value))

# Function to clear the entry field
def clear():
    entry.delete(0, tk.END)

# Function to calculate the result
def calculate():
    try:
        result = eval(entry.get())  # Evaluates the expression in the entry field
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Create the main window
root = tk.Tk()
root.title("Calculator")

# Entry widget to display the input and result
entry = tk.Entry(root, width=16, font=("Arial", 24), borderwidth=2, relief="solid", justify="right")
entry.grid(row=0, column=0, columnspan=4)

# Buttons for numbers and operations
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("0", 4, 1),
    ("+", 1, 3), ("-", 2, 3), ("*", 3, 3), ("/", 4, 3),
    ("C", 4, 0), ("=", 4, 2), (".", 5, 0)
]

# Add buttons to the grid
for (text, row, col) in buttons:
    if text == "=":
        button = tk.Button(root, text=text, width=10, height=3, font=("Arial", 18), command=calculate)
    elif text == "C":
        button = tk.Button(root, text=text, width=10, height=3, font=("Arial", 18), command=clear)
    else:
        button = tk.Button(root, text=text, width=10, height=3, font=("Arial", 18), command=lambda value=text: button_click(value))
    button.grid(row=row, column=col)

# Start the main loop
root.mainloop()
