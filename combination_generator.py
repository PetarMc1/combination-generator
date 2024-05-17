import itertools
import tkinter as tk
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText
import pyperclip
import os
import sys

def generate_combinations(input_string, combination_length):
    combinations = itertools.product(input_string, repeat=combination_length)
    unique_combinations = set(combinations)
    return unique_combinations

def display_combinations(combinations, output_area):
    combinations_str = "\n".join("".join(combination) for combination in combinations)
    output_area.config(state=tk.NORMAL)
    output_area.delete(1.0, tk.END)
    output_area.insert(tk.END, combinations_str)
    output_area.config(state=tk.DISABLED)
    return combinations_str

def resource_path(relative_path):
    try:
        # PyInstaller creates a temporary folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def main():
    root = tk.Tk()
    
    icon_path = resource_path('Assets/logo.ico')
    root.iconbitmap(icon_path)
    
    root.title("Combination Generator")

    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=1)
    root.grid_rowconfigure(3, weight=1)

    input_label = tk.Label(root, text="String:")
    input_label.grid(row=0, column=0, padx=10, pady=5, sticky=tk.E)

    input_entry = tk.Entry(root, width=50)
    input_entry.grid(row=0, column=1, padx=10, pady=5, sticky=tk.W)

    length_label = tk.Label(root, text="Count:")
    length_label.grid(row=1, column=0, padx=10, pady=5, sticky=tk.E)

    length_spinbox = tk.Spinbox(root, from_=1, to=10, width=5)
    length_spinbox.grid(row=1, column=1, padx=10, pady=5, sticky=tk.W)

    output_label = tk.Label(root, text="Output:")
    output_label.grid(row=2, column=0, padx=10, pady=5, sticky=tk.NE)

    output_area = ScrolledText(root, wrap=tk.WORD, width=50, height=20, state=tk.DISABLED)
    output_area.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky=tk.NSEW)

    def on_generate():
        input_string = input_entry.get()
        try:
            combination_length = int(length_spinbox.get())
            combinations = generate_combinations(input_string, combination_length)
            combinations_str = display_combinations(combinations, output_area)
            copy_button.config(command=lambda: copy_to_clipboard(combinations_str))
        except ValueError:
            messagebox.showerror("Invalid input", "Please enter a valid number for combination length.")

    def copy_to_clipboard(combinations_str):
        pyperclip.copy(combinations_str)
        messagebox.showinfo("Copied", "Combinations copied to clipboard!")

    generate_button = tk.Button(root, text="Generate", command=on_generate)
    generate_button.grid(row=4, column=1, padx=10, pady=10, sticky=tk.W)

    copy_button = tk.Button(root, text="Copy to Clipboard")
    copy_button.grid(row=2, column=1, padx=10, pady=5, sticky=tk.W)

    root.mainloop()

if __name__ == "__main__":
    main()
