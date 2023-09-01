import tkinter as tk
from tkinter import ttk
from calculator.profit_calculator import ProfitCalculator
from calculator.savings_calculator import SavingsCalculator
from calculator.invest_calculator import InvestmentCalculator

def toggle_frame(event):
    selected_calculator = calculator_type_var.get()
    if selected_calculator == "Sparziel Rechner":
        profit_frame.frame.grid_remove()
        investment_frame.frame.grid_remove()
        savings_frame.frame.grid()
    elif selected_calculator == "Gewinn Rechner":
        savings_frame.frame.grid_remove()
        investment_frame.frame.grid_remove()
        profit_frame.frame.grid()
    elif selected_calculator == "Investitionsrechner":
        profit_frame.frame.grid_remove()
        savings_frame.frame.grid_remove()
        investment_frame.frame.grid()

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
calculator_type_combo = ttk.Combobox(main_frame, textvariable=calculator_type_var,
                                    values=["Gewinn Rechner", "Sparziel Rechner", "Investitionsrechner"])
calculator_type_combo.grid(row=0, column=1, padx=10, pady=5)

# Create instances of the calculator classes
profit_frame = ProfitCalculator(main_frame)
savings_frame = SavingsCalculator(main_frame)
investment_frame = InvestmentCalculator(main_frame)

# Bind the function to the combo box selection event
calculator_type_combo.bind("<<ComboboxSelected>>", toggle_frame)

# Start the GUI
root.mainloop()
