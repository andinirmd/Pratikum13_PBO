import tkinter as tk
from tkinter import messagebox

def divide_numbers():
    try:
        num1 = int(entry_num1.get())
        num2 = int(entry_num2.get())
        result = num1 / num2
        label_result.config(text=f"Result: {result}")
    except ZeroDivisionError:
        messagebox.showerror("Error", "Division by zero is not allowed.")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")

def reset():
    entry_num1.delete(0, tk.END)
    entry_num2.delete(0, tk.END)
    label_result.config(text="Result:")

# Membuat jendela utama Tkinter
root = tk.Tk()
root.title("Exception Handling in Division")

# Label dan entry untuk angka pertama
tk.Label(root, text="Number 1:").pack()
entry_num1 = tk.Entry(root)
entry_num1.pack()

# Label dan entry untuk angka kedua
tk.Label(root, text="Number 2:").pack()
entry_num2 = tk.Entry(root)
entry_num2.pack()

# Tombol untuk membagi
button_divide = tk.Button(root, text="Divide", command=divide_numbers)
button_divide.pack()

# Tombol untuk mereset
button_reset = tk.Button(root, text="Reset", command=reset)
button_reset.pack()

# Label untuk menampilkan hasil
label_result = tk.Label(root, text="Result:")
label_result.pack()

# Menjalankan aplikasi
root.mainloop()