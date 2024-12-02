import tkinter as tk

# Kelas induk Animal
class Animal:
    def make_sound(self):
        return "Some sound"

# Kelas turunan Bird
class Bird(Animal):
    def make_sound(self):
        return "Tweet tweet"

# Kelas turunan Dog
class Dog(Animal):
    def make_sound(self):
        return "Woof woof"

# Kelas turunan Duck (Bebek)
class Duck(Animal):
    def make_sound(self):
        return "Quack quack"

# Kelas turunan WildCat (Harimau)
class WildCat(Animal):
    def make_sound(self):
        return "Roar roar"

# Fungsi untuk menampilkan suara berdasarkan jenis hewan yang dipilih
def show_sound(animal):
    label_result.config(text=animal.make_sound())

# Membuat jendela utama Tkinter
root = tk.Tk()
root.title("Polimorfisme di Tkinter")

# Label untuk menampilkan hasil suara
label_result = tk.Label(root, text="Klik salah satu tombol untuk mendengar suara hewan.", font=("Arial", 14))
label_result.pack(pady=20)

# Tombol untuk memilih burung
button_bird = tk.Button(root, text="Burung", font=("Arial", 12), command=lambda: show_sound(Bird()))
button_bird.pack(pady=10)

# Tombol untuk memilih anjing
button_dog = tk.Button(root, text="Anjing", font=("Arial", 12), command=lambda: show_sound(Dog()))
button_dog.pack(pady=10)

# Tombol untuk memilih Bebek
button_duck = tk.Button(root, text="Bebek", font=("Arial", 12), command=lambda: show_sound(Duck()))
button_duck.pack(pady=10)

# Tombol untuk memilih Harimau
button_wildcat = tk.Button(root, text="Harimau", font=("Arial", 12), command=lambda: show_sound(WildCat()))
button_wildcat.pack(pady=10)

# Menjalankan aplikasi
root.mainloop()