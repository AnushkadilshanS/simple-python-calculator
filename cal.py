import tkinter as tk
from tkinter import messagebox

# Function to handle button click
def button_click(value):
    current = entry.get()
    if value == "=":
        try:
            result = eval(current)
            entry.delete(0, tk.END)
            entry.insert(0, str(result))
        except Exception as e:
            messagebox.showerror("Error", "Invalid Input!")
    elif value == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, value)

# Create the main window
root = tk.Tk()
root.title("Calculator")
root.geometry("350x500")
root.resizable(False, False)
root.configure(bg="#2c3e50")

# Entry widget to display the current calculation
entry = tk.Entry(root, font=("Arial", 24), bd=10, insertwidth=2, width=14, borderwidth=0, justify='right', bg="#ecf0f1", fg="#2c3e50")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Button styles
btn_style = {
    "font": ("Arial", 18),
    "fg": "#ffffff",
    "bg": "#34495e",
    "relief": "flat",
    "activebackground": "#2c3e50",
    "activeforeground": "#ffffff",
    "padx": 20,
    "pady": 20,
    "bd": 0
}

# Special button styles (C and =)
special_btn_style = {
    "bg": "#e74c3c",
    "activebackground": "#c0392b"
}

equals_btn_style = {
    "bg": "#27ae60",
    "activebackground": "#229954"
}

# Button layout
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]

# Create and place buttons
row_val = 1
col_val = 0
for button in buttons:
    style = btn_style.copy()  # Default button style
    if button == "C":
        style.update(special_btn_style)  # Special style for "C"
    elif button == "=":
        style.update(equals_btn_style)  # Special style for "="

    btn = tk.Button(root, text=button, **style, command=lambda b=button: button_click(b))
    btn.grid(row=row_val, column=col_val, padx=5, pady=5)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Run the application
root.mainloop()
