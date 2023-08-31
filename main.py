import tkinter as tk
from tkinter import ttk

def calculate_profit():
    try:
        expenses = float(expenses_entry.get())
        incomes = float(incomes_entry.get())
        variable_expenses = float(variable_expenses_entry.get())
        variable_incomes = float(variable_incomes_entry.get())
        
        total_expenses = expenses - variable_expenses
        total_incomes = incomes - variable_incomes
        profit = total_incomes - total_expenses
        
        result_label.config(text=f"Gewinn: {profit:.2f} €")
    except ValueError:
        result_label.config(text="Bitte gültige Zahlen eingeben")

def calculate_savings_goal():
    try:
        current_savings = float(current_savings_entry.get())
        monthly_savings = float(monthly_savings_entry.get())
        target_amount = float(target_amount_entry.get())
        
        months_needed = (target_amount - current_savings) / monthly_savings
        result_savings_label.config(text=f"Benötigte Monate: {months_needed:.2f}")
    except ValueError:
        result_savings_label.config(text="Bitte gültige Zahlen eingeben")

def toggle_frame(event):
    if calculator_type_var.get() == "Sparziel Rechner":
        profit_frame.grid_remove()
        savings_frame.grid()
    else:
        savings_frame.grid_remove()
        profit_frame.grid()

# GUI Setup
def center_window(root, width, height):

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()


    x = (screen_width - width) // 2
    y = (screen_height - height) // 2

    root.geometry(f"{width}x{height}+{x}+{y}")

root = tk.Tk()
root.title("Finanzrechner")
root.iconbitmap("calc.ico")

window_width = 400
window_height = 300

center_window(root, window_width, window_height)

# Frame for the main content
main_frame = ttk.Frame(root)
main_frame.pack(padx=20, pady=20)

# Option menu for choosing the calculator type
calculator_type_label = ttk.Label(main_frame, text="Auswahl:")
calculator_type_label.grid(row=0, column=0, sticky="w")

calculator_type_var = tk.StringVar()
calculator_type_combo = ttk.Combobox(main_frame, textvariable=calculator_type_var, values=["Gewinn Rechner", "Sparziel Rechner"])
calculator_type_combo.grid(row=0, column=1, padx=10, pady=5)

# Frame for the profit calculator
profit_frame = ttk.LabelFrame(main_frame, text="Gewinn Rechner")
profit_frame.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="w")

expenses_label = ttk.Label(profit_frame, text="Ausgaben:")
expenses_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
expenses_entry = ttk.Entry(profit_frame)
expenses_entry.grid(row=0, column=1, padx=5, pady=5)

incomes_label = ttk.Label(profit_frame, text="Einnahmen:")
incomes_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
incomes_entry = ttk.Entry(profit_frame)
incomes_entry.grid(row=1, column=1, padx=5, pady=5)

variable_expenses_label = ttk.Label(profit_frame, text="Variable Ausgaben:")
variable_expenses_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
variable_expenses_entry = ttk.Entry(profit_frame)
variable_expenses_entry.grid(row=2, column=1, padx=5, pady=5)

variable_incomes_label = ttk.Label(profit_frame, text="Variable Einnahmen:")
variable_incomes_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")
variable_incomes_entry = ttk.Entry(profit_frame)
variable_incomes_entry.grid(row=3, column=1, padx=5, pady=5)

calculate_button = ttk.Button(profit_frame, text="Berechnen", command=calculate_profit)
calculate_button.grid(row=4, column=0, columnspan=2, pady=10)

result_label = ttk.Label(profit_frame, text="Gewinn: ")
result_label.grid(row=5, column=0, columnspan=2)

# Frame for the savings goal calculator
savings_frame = ttk.LabelFrame(main_frame, text="Sparziel Rechner")
savings_frame.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="w")
savings_frame.grid_remove()

current_savings_label = ttk.Label(savings_frame, text="Aktuelles Sparguthaben:")
current_savings_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
current_savings_entry = ttk.Entry(savings_frame)
current_savings_entry.grid(row=0, column=1, padx=5, pady=5)

monthly_savings_label = ttk.Label(savings_frame, text="Monatliche Einzahlung:")
monthly_savings_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
monthly_savings_entry = ttk.Entry(savings_frame)
monthly_savings_entry.grid(row=1, column=1, padx=5, pady=5)

target_amount_label = ttk.Label(savings_frame, text="Zielbetrag:")
target_amount_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
target_amount_entry = ttk.Entry(savings_frame)
target_amount_entry.grid(row=2, column=1, padx=5, pady=5)

calculate_savings_button = ttk.Button(savings_frame, text="Berechnen", command=calculate_savings_goal)
calculate_savings_button.grid(row=3, column=0, columnspan=2, pady=10)

result_savings_label = ttk.Label(savings_frame, text="Benötigte Monate: ")
result_savings_label.grid(row=4, column=0, columnspan=2)

calculator_type_combo.bind("<<ComboboxSelected>>", toggle_frame)

# Start the GUI
root.mainloop()

