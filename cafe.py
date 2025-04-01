import tkinter as tk
from tkinter import messagebox

def place_order():
    order_summary = "Your Order:\n"
    total_cost = 0
    for item, price, entry in items:
        quantity = entry.get()
        if quantity.isdigit() and int(quantity) > 0:
            cost = int(quantity) * price
            total_cost += cost
            order_summary += f"{item} x {quantity} = ₹-{cost}\n"
    
    if total_cost > 0:
        order_summary += f"\nTotal Cost: ₹{total_cost}"
        messagebox.showinfo("Order Summary", order_summary)
    else:
        messagebox.showwarning("Order Warning", "Please select at least one item.")

# Creating main window
root = tk.Tk()
root.title("Cafe Menu")
root.geometry("300x250")
root.config(background="black")

# Title label
title_label = tk.Label(root, text="WELCOME TO THE CAFE", font=("Arial", 14, "bold"))
title_label.grid(row=0, column=0, columnspan=3, pady=5)


# Table headers
headers = ["Items", "Price ($)", "Order"]
for i, header in enumerate(headers):
    tk.Label(root, text=header, font=("Arial", 10, "bold"), width=10).grid(row=1, column=i, padx=5, pady=5)

# Menu items
menu = [
    ("Coffee", 30),
    ("Maggie", 40),
    ("Burger", 50),
    ("Tea", 10),
    ("Bun Maska", 20),
]

items = []
for i, (item, price) in enumerate(menu, start=2):
    tk.Label(root, text=item, font=("Arial", 10), width=10).grid(row=i, column=0)
    tk.Label(root, text=f"₹{price}", font=("Arial", 10), width=10).grid(row=i, column=1)
    entry = tk.Entry(root, width=5)
    entry.grid(row=i, column=2)
    items.append((item, price, entry))

# Order button
order_button = tk.Button(root, text="Place Order", command=place_order)
order_button.grid(row=len(menu) + 2, column=0, columnspan=3, pady=10)

# Run application
root.mainloop()
