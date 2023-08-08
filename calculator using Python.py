import tkinter as tk
import math

def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(number))

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def calculate_trig(func):
    try:
        value = eval(func + "(" + entry.get() + ")")
        entry.delete(0, tk.END)
        entry.insert(0, value)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Create the main window
root = tk.Tk()
root.title("Calculator")

# Entry widget to display the input and results
entry = tk.Entry(root, width=20, font=('Arial', 20))
entry.grid(row=0, column=0, columnspan=4)

# Buttons
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3),
    ('sin', 5, 0), ('cos', 5, 1), ('tan', 5, 2), ('', 5, 3),
]

for (text, row, col) in buttons:
    if text:
        button = tk.Button(root, text=text, width=5, height=2,
                           font=('Arial', 15),
                           command=lambda t=text: button_click(t) if t != '=' else calculate())
        button.grid(row=row, column=col)
    else:
        button = tk.Button(root, text='', width=5, height=2, state=tk.DISABLED)
        button.grid(row=row, column=col)

# Trigonometric buttons
trig_functions = ['sin', 'cos', 'tan']
for i, func in enumerate(trig_functions):
    trig_button = tk.Button(root, text=func, width=5, height=2,
                            font=('Arial', 15),
                            command=lambda f=func: calculate_trig(f))
    trig_button.grid(row=6, column=i)

# Start the GUI event loop
root.mainloop()
