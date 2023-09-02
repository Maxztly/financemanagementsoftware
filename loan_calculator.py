import tkinter as tk
from tkinter import ttk

class LoanCalculator:
    def __init__(self, parent_frame):
        self.frame = ttk.LabelFrame(parent_frame, text="Kreditrechner")
        self.frame.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="w")
        self.frame.grid_remove()

        loan_amount_label = ttk.Label(self.frame, text="Darlehensbetrag (€):")
        loan_amount_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.loan_amount_entry = ttk.Entry(self.frame)
        self.loan_amount_entry.grid(row=0, column=1, padx=5, pady=5)

        interest_rate_label = ttk.Label(self.frame, text="Zinssatz (% pro Jahr):")
        interest_rate_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.interest_rate_entry = ttk.Entry(self.frame)
        self.interest_rate_entry.grid(row=1, column=1, padx=5, pady=5)

        loan_term_label = ttk.Label(self.frame, text="Laufzeit (Jahre):")
        loan_term_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.loan_term_entry = ttk.Entry(self.frame)
        self.loan_term_entry.grid(row=2, column=1, padx=5, pady=5)

        calculate_button = ttk.Button(self.frame, text="Berechnen", command=self.calculate_loan)
        calculate_button.grid(row=3, column=0, columnspan=2, pady=10)

        self.result_label = ttk.Label(self.frame, text="Monatliche Rate: ")
        self.result_label.grid(row=4, column=0, columnspan=2)

    def calculate_loan(self):
        try:
            loan_amount = float(self.loan_amount_entry.get())
            annual_interest_rate = float(self.interest_rate_entry.get()) / 100  # Convert percentage to decimal
            loan_term = int(self.loan_term_entry.get())
            
            monthly_interest_rate = annual_interest_rate / 12
            num_payments = loan_term * 12
            
            monthly_payment = (loan_amount * monthly_interest_rate) / (1 - (1 + monthly_interest_rate) ** -num_payments)
            
            self.result_label.config(text=f"Monatliche Rate: {monthly_payment:.2f} €")
        except ValueError:
            self.result_label.config(text="Bitte gültige Zahlen eingeben")


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Kreditrechner")
    app = LoanCalculator(root)
    root.mainloop()
