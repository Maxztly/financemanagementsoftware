import tkinter as tk
from tkinter import ttk
from profit_calculator import ProfitCalculator
from calculator.savings_calculator import SavingsCalculator

def toggle_frame(event):
    if calculator_type_var.get() == "Sparziel Rechner":
        profit_frame.frame.grid_remove()
        savings_frame.frame.grid()
    else:
        savings_frame.frame.grid_remove()
        profit_frame.frame.grid()

# GUI Setup
root = tk.Tk()
root.title("Finanzmanagement")

# Frame for the main content
main_frame = ttk.Frame(root)
main_frame.pack(padx=20, pady=20)

# Option menu for choosing the calculator type
calculator_type_label = ttk.Label(main_frame, text="Auswahl:")
calculator_type_label.grid(row=0, column=0, sticky="w")

calculator_type_var = tk.StringVar()
calculator_type_combo = ttk.Combobox(main_frame, textvariable=calculator_type_var, values=["Gewinn Rechner", "Sparziel Rechner"])
calculator_type_combo.grid(row=0, column=1, padx=10, pady=5)

# Create instances of the calculator classes
profit_frame = ProfitCalculator(main_frame)
savings_frame = SavingsCalculator(main_frame)

# Bind the function to the combo box selection event
calculator_type_combo.bind("<<ComboboxSelected>>", toggle_frame)

# Start the GUI
root.mainloop()
