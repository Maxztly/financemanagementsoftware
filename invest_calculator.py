import tkinter as tk
from tkinter import ttk

class InvestmentCalculator:
    def __init__(self, parent_frame):
        self.frame = ttk.LabelFrame(parent_frame, text="Investitionsrechner")
        self.frame.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="w")
        self.frame.grid_remove()

        initial_investment_label = ttk.Label(self.frame, text="Einmalige Einzahlung:")
        initial_investment_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.initial_investment_entry = ttk.Entry(self.frame)
        self.initial_investment_entry.grid(row=0, column=1, padx=5, pady=5)

        regular_payment_label = ttk.Label(self.frame, text="Regelmäßige Zahlung:")
        regular_payment_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.regular_payment_entry = ttk.Entry(self.frame)
        self.regular_payment_entry.grid(row=1, column=1, padx=5, pady=5)

        annual_return_label = ttk.Label(self.frame, text="Erwartete Rendite (% pro Jahr):")
        annual_return_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.annual_return_entry = ttk.Entry(self.frame)
        self.annual_return_entry.grid(row=2, column=1, padx=5, pady=5)

        investment_duration_label = ttk.Label(self.frame, text="Anlagedauer (Jahre):")
        investment_duration_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")
        self.investment_duration_entry = ttk.Entry(self.frame)
        self.investment_duration_entry.grid(row=3, column=1, padx=5, pady=5)

        calculate_button = ttk.Button(self.frame, text="Berechnen", command=self.calculate_investment)
        calculate_button.grid(row=4, column=0, columnspan=2, pady=10)

        self.result_label = ttk.Label(self.frame, text="Endwert der Investition: ")
        self.result_label.grid(row=5, column=0, columnspan=2)

    def calculate_investment(self):
        try:
            initial_investment = float(self.initial_investment_entry.get())
            regular_payment = float(self.regular_payment_entry.get())
            annual_return = float(self.annual_return_entry.get()) / 100  # Convert percentage to decimal
            investment_duration = int(self.investment_duration_entry.get())
            
            future_value = initial_investment
            for year in range(investment_duration):
                future_value += regular_payment
                future_value *= (1 + annual_return)
            
            self.result_label.config(text=f"Endwert der Investition: {future_value:.2f} €")
        except ValueError:
            self.result_label.config(text="Bitte gültige Zahlen eingeben")


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Investitionsrechner")
    app = InvestmentCalculator(root)
    root.mainloop()
