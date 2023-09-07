import tkinter as tk
from tkinter import ttk

class RealReturnCalculator:
    def __init__(self, parent_frame):
        self.frame = ttk.LabelFrame(parent_frame, text="Realrendite-Rechner")
        self.frame.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="w")
        self.frame.grid_remove()

        initial_investment_label = ttk.Label(self.frame, text="Startkapital (€):")
        initial_investment_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.initial_investment_entry = ttk.Entry(self.frame)
        self.initial_investment_entry.grid(row=0, column=1, padx=5, pady=5)

        current_investment_label = ttk.Label(self.frame, text="Aktueller Kapitalstand (€):")
        current_investment_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.current_investment_entry = ttk.Entry(self.frame)
        self.current_investment_entry.grid(row=1, column=1, padx=5, pady=5)

        investment_duration_label = ttk.Label(self.frame, text="Anlagedauer (Jahre):")
        investment_duration_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.investment_duration_entry = ttk.Entry(self.frame)
        self.investment_duration_entry.grid(row=2, column=1, padx=5, pady=5)

        inflation_rate_label = ttk.Label(self.frame, text="Durchschnittliche Inflationsrate (% pro Jahr):")
        inflation_rate_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")
        self.inflation_rate_entry = ttk.Entry(self.frame)
        self.inflation_rate_entry.grid(row=3, column=1, padx=5, pady=5)

        calculate_button = ttk.Button(self.frame, text="Berechnen", command=self.calculate_real_return)
        calculate_button.grid(row=4, column=0, columnspan=2, pady=10)

        self.normal_return_label = ttk.Label(self.frame, text="Normale Rendite (%): ")
        self.normal_return_label.grid(row=5, column=0, columnspan=2)

        self.real_return_label = ttk.Label(self.frame, text="Realrendite (%): ")
        self.real_return_label.grid(row=6, column=0, columnspan=2)

        self.normal_return_absolute_label = ttk.Label(self.frame, text="Absolute normale Rendite (€): ")
        self.normal_return_absolute_label.grid(row=7, column=0, columnspan=2)

        self.real_return_absolute_label = ttk.Label(self.frame, text="Absolute Realrendite (€): ")
        self.real_return_absolute_label.grid(row=8, column=0, columnspan=2)

    def calculate_real_return(self):
        try:
            initial_investment = float(self.initial_investment_entry.get())
            current_investment = float(self.current_investment_entry.get())
            investment_duration = int(self.investment_duration_entry.get())
            inflation_rate = float(self.inflation_rate_entry.get()) / 100  # Convert percentage to decimal

            normal_return = ((current_investment - initial_investment) / initial_investment) * 100
            real_return = (1 + normal_return / 100) / (1 + inflation_rate) - 1
            normal_return_percentage = normal_return
            real_return_percentage = real_return * 100

            normal_return_absolute = (normal_return / 100) * initial_investment
            real_return_absolute = (real_return) * initial_investment

            self.normal_return_label.config(text=f"Normale Rendite (%): {normal_return_percentage:.2f}%")
            self.real_return_label.config(text=f"Realrendite (%): {real_return_percentage:.2f}%")
            self.normal_return_absolute_label.config(text=f"Absolute normale Rendite (€): {normal_return_absolute:.2f} €")
            self.real_return_absolute_label.config(text=f"Absolute Realrendite (€): {real_return_absolute:.2f} €")
        except ValueError:
            self.normal_return_label.config(text="Bitte gültige Zahlen eingeben")
            self.real_return_label.config(text="Bitte gültige Zahlen eingeben")


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Realrendite-Rechner")
    app = RealReturnCalculator(root)
    root.mainloop()