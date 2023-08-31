import tkinter as tk
from tkinter import ttk

class SavingsCalculator:
    def __init__(self, parent_frame):
        self.frame = ttk.LabelFrame(parent_frame, text="Sparziel Rechner")
        self.frame.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="w")
        self.frame.grid_remove()

        current_savings_label = ttk.Label(self.frame, text="Aktuelles Sparguthaben:")
        current_savings_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.current_savings_entry = ttk.Entry(self.frame)
        self.current_savings_entry.grid(row=0, column=1, padx=5, pady=5)

        monthly_savings_label = ttk.Label(self.frame, text="Monatliche Einzahlung:")
        monthly_savings_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.monthly_savings_entry = ttk.Entry(self.frame)
        self.monthly_savings_entry.grid(row=1, column=1, padx=5, pady=5)

        target_amount_label = ttk.Label(self.frame, text="Zielbetrag:")
        target_amount_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.target_amount_entry = ttk.Entry(self.frame)
        self.target_amount_entry.grid(row=2, column=1, padx=5, pady=5)

        calculate_button = ttk.Button(self.frame, text="Berechnen", command=self.calculate_savings_goal)
        calculate_button.grid(row=3, column=0, columnspan=2, pady=10)

        self.result_savings_label = ttk.Label(self.frame, text="Benötigte Monate: ")
        self.result_savings_label.grid(row=4, column=0, columnspan=2)

    def calculate_savings_goal(self):
        try:
            current_savings = float(self.current_savings_entry.get())
            monthly_savings = float(self.monthly_savings_entry.get())
            target_amount = float(self.target_amount_entry.get())
            
            months_needed = (target_amount - current_savings) / monthly_savings
            self.result_savings_label.config(text=f"Benötigte Monate: {months_needed:.2f}")
        except ValueError:
            self.result_savings_label.config(text="Bitte gültige Zahlen eingeben")


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Sparziel Rechner")
    app = SavingsCalculator(root)
    root.mainloop()
