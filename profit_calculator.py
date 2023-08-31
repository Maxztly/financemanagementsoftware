import tkinter as tk
from tkinter import ttk

class ProfitCalculator:
    def __init__(self, parent_frame):
        self.frame = ttk.LabelFrame(parent_frame, text="Gewinn Rechner")
        self.frame.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="w")

        expenses_label = ttk.Label(self.frame, text="Ausgaben:")
        expenses_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.expenses_entry = ttk.Entry(self.frame)
        self.expenses_entry.grid(row=0, column=1, padx=5, pady=5)

        incomes_label = ttk.Label(self.frame, text="Einnahmen:")
        incomes_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.incomes_entry = ttk.Entry(self.frame)
        self.incomes_entry.grid(row=1, column=1, padx=5, pady=5)

        variable_expenses_label = ttk.Label(self.frame, text="Variable Ausgaben:")
        variable_expenses_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.variable_expenses_entry = ttk.Entry(self.frame)
        self.variable_expenses_entry.grid(row=2, column=1, padx=5, pady=5)

        variable_incomes_label = ttk.Label(self.frame, text="Variable Einnahmen:")
        variable_incomes_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")
        self.variable_incomes_entry = ttk.Entry(self.frame)
        self.variable_incomes_entry.grid(row=3, column=1, padx=5, pady=5)

        calculate_button = ttk.Button(self.frame, text="Berechnen", command=self.calculate_profit)
        calculate_button.grid(row=4, column=0, columnspan=2, pady=10)

        self.result_label = ttk.Label(self.frame, text="Gewinn: ")
        self.result_label.grid(row=5, column=0, columnspan=2)

    def calculate_profit(self):
        try:
            expenses = float(self.expenses_entry.get())
            incomes = float(self.incomes_entry.get())
            variable_expenses = float(self.variable_expenses_entry.get())
            variable_incomes = float(self.variable_incomes_entry.get())
            
            total_expenses = expenses - variable_expenses
            total_incomes = incomes - variable_incomes
            profit = total_incomes - total_expenses
            
            self.result_label.config(text=f"Gewinn: {profit:.2f} €")
        except ValueError:
            self.result_label.config(text="Bitte gültige Zahlen eingeben")


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Gewinn Rechner")
    app = ProfitCalculator(root)
    root.mainloop()
