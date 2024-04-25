import tkinter as tk
from tkinter import simpledialog, messagebox, ttk
import random
import pyfiglet
import pyperclip

class ASCIICraftGUI:
    def __init__(self, master):
        self.master = master
        master.title("ASCIICraft")
        master.geometry("800x600")
        master.configure(bg="#1c1c1c")  # Set background color

        self.label = tk.Label(master, text=self.greet(), font=("Courier", 20), fg="#ff4500", bg="#1c1c1c")  # Set text color and background color
        self.label.pack(pady=20)

        self.text_input = tk.Entry(master, width=50, font=("Courier", 14), bg="#4d4d4d", fg="#ff4500", insertbackground="#ff4500")  # Set input field style
        self.text_input.pack(pady=20)

        self.fonts = [
            "Standard", "Slant", "Big", "Banner", "Block", "Bubble", "Chunky", "Contessa", "Cosmic", "Doh",
            "Efti Chess", "Efti Font", "Efti Italic", "Fire Font-k", "Graceful", "Graffiti", "Impossible",
            "Isometric1", "Larry 3D", "Letters"
        ]
        self.font_var = tk.StringVar(master)
        self.font_var.set(self.fonts[0])

        self.font_menu = tk.OptionMenu(master, self.font_var, *self.fonts)
        self.font_menu.config(font=("Courier", 14), bg="#4d4d4d", fg="#ff4500", activebackground="#ff4500", activeforeground="#4d4d4d")  # Set dropdown menu style
        self.font_menu.pack(pady=10)

        self.convert_button = tk.Button(master, text="Generate ASCII Art", command=self.convert_to_ascii, font=("Courier", 14), bg="#ff4500", fg="#1c1c1c", activebackground="#1c1c1c", activeforeground="#ff4500")  # Set button style
        self.convert_button.pack(pady=20)

        self.random_button = tk.Button(master, text="Generate Random ASCII Art", command=self.generate_random_ascii, font=("Courier", 14), bg="#ff4500", fg="#1c1c1c", activebackground="#1c1c1c", activeforeground="#ff4500")  # Set button style
        self.random_button.pack(pady=20)

        self.output_frame = tk.Frame(master, bg="#1c1c1c")
        self.output_frame.pack(pady=20)

        self.output_label = tk.Text(self.output_frame, height=10, width=100, wrap=tk.NONE, font=("Courier", 16), bg="#4d4d4d", fg="#ff4500")  # Set output text style
        self.output_label.pack(side=tk.LEFT)

        self.scrollbar = tk.Scrollbar(self.output_frame, command=self.output_label.xview, orient=tk.HORIZONTAL)
        self.scrollbar.pack(side=tk.BOTTOM, fill=tk.X)
        self.output_label.config(xscrollcommand=self.scrollbar.set)

        self.copy_button = tk.Button(master, text="Copy Output", command=self.copy_output, font=("Courier", 14), bg="#ff4500", fg="#1c1c1c", activebackground="#1c1c1c", activeforeground="#ff4500")  # Set button style
        self.copy_button.pack(pady=10)

        self.quit_button = tk.Button(master, text="Exit", command=master.quit, font=("Courier", 14), bg="#ff4500", fg="#1c1c1c", activebackground="#1c1c1c", activeforeground="#ff4500")  # Set button style
        self.quit_button.pack(pady=20)

    def greet(self):
        greetings = ["Fear me!", "What do you want?", "Bow before me!", "I am power!"]
        return random.choice(greetings)

    def convert_to_ascii(self):
        user_input = self.text_input.get()
        selected_font = self.font_var.get()
        if user_input:
            ascii_art = pyfiglet.figlet_format(user_input, font=selected_font)
            self.output_label.delete('1.0', tk.END)
            self.output_label.insert(tk.END, ascii_art)
        else:
            messagebox.showinfo("Error", "Please enter some text to convert.")

    def generate_random_ascii(self):
        phrases = [
            "Fear the unknown",
            "Conquer your fears",
            "Strength in adversity",
            "Victory is inevitable",
            "Rise above the rest",
            "Unleash your power",
            "Embrace the darkness",
            "Face your destiny",
            "Dominate the battlefield",
            "Be relentless"
        ]
        random_phrase = random.choice(phrases)
        selected_font = self.font_var.get()
        ascii_art = pyfiglet.figlet_format(random_phrase, font=selected_font)
        self.output_label.delete('1.0', tk.END)
        self.output_label.insert(tk.END, ascii_art)

    def copy_output(self):
        output_text = self.output_label.get('1.0', tk.END)
        pyperclip.copy(output_text)
        messagebox.showinfo("Copy", "Output copied to clipboard.")

root = tk.Tk()
app = ASCIICraftGUI(root)
root.mainloop()
