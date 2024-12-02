import tkinter as tk
from tkinter import messagebox

class BankAccount:
    def __init__(self):
        self._balance = 0  # Private attribute

    def get_balance(self):
        return self._balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
        else:
            raise ValueError("Invalid deposit amount!")

# Function to add balance
def add_balance():
    try:
        amount = int(entry_amount.get())
        account.deposit(amount)
        label_balance.config(text=f"Balance: {account.get_balance()}")
    except ValueError as e:
        messagebox.showerror("Error", str(e))

# Function to reset balance and input
def reset():
    entry_amount.delete(0, tk.END)  # Clear entry field
    label_balance.config(text=f"Balance: {account.get_balance()}")  # Update balance label (optional)

# Create the main Tkinter window
root = tk.Tk()
root.title("Data Hiding in BankAccount")

# Create BankAccount object
account = BankAccount()

# Label to display balance
label_balance = tk.Label(root, text=f"Balance: {account.get_balance()}")
label_balance.pack()

# Entry for deposit amount
entry_amount = tk.Entry(root)
entry_amount.pack()

# Button for deposit
button_deposit = tk.Button(root, text="Deposit", command=add_balance)
button_deposit.pack()

# Button for reset 
button_reset = tk.Button(root, text="Reset", command=reset)
button_reset.pack()  

# Run the application
root.mainloop()