import tkinter as tk
from tkinter import ttk
from calculator.profit_calculator import ProfitCalculator
from calculator.savings_calculator import SavingsCalculator
from calculator.invest_calculator import InvestmentCalculator
from calculator.loan_calculator import LoanCalculator
from calculator.rental_yield_calculator import RentalYieldCalculator
from calculator.inflation_calculator import InflationCalculator
from calculator.real_return_calculator import RealReturnCalculator

def toggle_frame(event):
    selected_calculator = calculator_type_var.get()
    if selected_calculator == "Sparziel Rechner":
        profit_frame.frame.grid_remove()
        investment_frame.frame.grid_remove()
        loan_frame.frame.grid_remove()
        rental_yield_frame.frame.grid_remove()
        inflation_frame.frame.grid_remove()
        real_return_frame.frame.grid_remove()
        savings_frame.frame.grid()
    elif selected_calculator == "Gewinn Rechner":
        savings_frame.frame.grid_remove()
        investment_frame.frame.grid_remove()
        loan_frame.frame.grid_remove()
        rental_yield_frame.frame.grid_remove()
        inflation_frame.frame.grid_remove()
        real_return_frame.frame.grid_remove()
        profit_frame.frame.grid()
    elif selected_calculator == "Investitionsrechner":
        profit_frame.frame.grid_remove()
        savings_frame.frame.grid_remove()
        loan_frame.frame.grid_remove()
        rental_yield_frame.frame.grid_remove()
        inflation_frame.frame.grid_remove()
        real_return_frame.frame.grid_remove()
        investment_frame.frame.grid()
    elif selected_calculator == "Kreditrechner":
        profit_frame.frame.grid_remove()
        savings_frame.frame.grid_remove()
        investment_frame.frame.grid_remove()
        loan_frame.frame.grid_remove()
        rental_yield_frame.frame.grid_remove()
        inflation_frame.frame.grid_remove()
        real_return_frame.frame.grid_remove()
        loan_frame.frame.grid()
    elif selected_calculator == "Mietrendite-Rechner":
        profit_frame.frame.grid_remove()
        savings_frame.frame.grid_remove()
        investment_frame.frame.grid_remove()
        loan_frame.frame.grid_remove()
        inflation_frame.frame.grid_remove()
        real_return_frame.frame.grid_remove()
        rental_yield_frame.frame.grid()
    elif selected_calculator == "Inflationsrechner":
        profit_frame.frame.grid_remove()
        savings_frame.frame.grid_remove()
        investment_frame.frame.grid_remove()
        loan_frame.frame.grid_remove()
        rental_yield_frame.frame.grid_remove()
        real_return_frame.frame.grid_remove()
        inflation_frame.frame.grid()
    elif selected_calculator == "Realrendite-Rechner":
        profit_frame.frame.grid_remove()
        savings_frame.frame.grid_remove()
        investment_frame.frame.grid_remove()
        loan_frame.frame.grid_remove()
        rental_yield_frame.frame.grid_remove()
        inflation_frame.frame.grid_remove()
        real_return_frame.frame.grid()

# GUI Setup
root = tk.Tk()
root.title("Finanzmanagement")
root.iconbitmap("calc.ico")
# Get the screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Calculate the X and Y position for the Tkinter window
x = (screen_width / 2) - (root.winfo_reqwidth() / 2)
y = (screen_height / 2) - (root.winfo_reqheight() / 2)

# Set the window's position
root.geometry("+%d+%d" % (x, y))

# Frame for the main content
main_frame = ttk.Frame(root)
main_frame.pack(padx=20, pady=20)

# Option menu for choosing the calculator type
calculator_type_label = ttk.Label(main_frame, text="Auswahl:")
calculator_type_label.grid(row=0, column=0, sticky="w")

calculator_type_var = tk.StringVar()
calculator_type_combo = ttk.Combobox(main_frame, textvariable=calculator_type_var,
                                    values=["Gewinn Rechner", "Sparziel Rechner", "Investitionsrechner", "Kreditrechner", "Mietrendite-Rechner", "Inflationsrechner", "Realrendite-Rechner"])
calculator_type_combo.grid(row=0, column=1, padx=10, pady=5)

# Create instances of the calculator classes
profit_frame = ProfitCalculator(main_frame)
savings_frame = SavingsCalculator(main_frame)
investment_frame = InvestmentCalculator(main_frame)
loan_frame = LoanCalculator(main_frame)
rental_yield_frame = RentalYieldCalculator(main_frame)
inflation_frame = InflationCalculator(main_frame)
real_return_frame = RealReturnCalculator(main_frame)

# Bind the function to the combo box selection event
calculator_type_combo.bind("<<ComboboxSelected>>", toggle_frame)

# Start the GUI
root.mainloop()
