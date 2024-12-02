import tkinter as tk
from tkinter import messagebox
from math import pi

class Shape:
    def area(self):
        return "Not implemented"

    def perimeter(self):
        return "Not implemented"

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return pi * self.radius ** 2

    def perimeter(self):
        return 2 * pi * self.radius

def calculate():
    try:
        shape_type = shape_var.get()
        if shape_type == "Rectangle":
            length = int(entry_param1.get())
            width = int(entry_param2.get())
            shape = Rectangle(length, width)
        elif shape_type == "Rectangle":
            radius = int(entry_param1.get())
            shape = Circle(radius)
        else:
            raise ValueError("Invalid shape")
        label_result.config(text=f"Area: {shape.area()}, Perimeter: {shape.perimeter()}")
    except ValueError as e:
        messagebox.showerror("Error", str(e))

def reset():
    shape_var.set("Rectangle")  # Reset pilihan bentuk ke default
    entry_param1.delete(0, tk.END)  # Hapus nilai pada entry pertama
    entry_param2.delete(0, tk.END)  # Hapus nilai pada entry kedua
    label_result.config(text="")  # Kosongkan label hasil

# Membuat jendela utama Tkinter
root = tk.Tk()
root.title("Overriding in Shapes")

# Variabel untuk menyimpan pilihan bentuk
shape_var = tk.StringVar(value="Rectangle")

# Radio button untuk memilih bentuk
tk.Radiobutton(root, text="Rectangle", variable=shape_var, value="Rectangle").pack()
tk.Radiobutton(root, text="Circle", variable=shape_var, value="Circle").pack()

# Label dan entry untuk parameter
tk.Label(root, text="Parameter 1:").pack()
entry_param1 = tk.Entry(root)
entry_param1.pack()

tk.Label(root, text="Parameter 2 (if Rectangle):").pack()
entry_param2 = tk.Entry(root)
entry_param2.pack()

# Tombol untuk menghitung dan mereset
button_calculate = tk.Button(root, text="Calculate", command=calculate)
button_calculate.pack()
button_reset = tk.Button(root, text="Reset", command=reset)
button_reset.pack()

# Label untuk menampilkan hasil
label_result = tk.Label(root)
label_result.pack()

# Menjalankan aplikasi
root.mainloop()