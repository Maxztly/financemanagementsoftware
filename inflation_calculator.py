import tkinter as tk
from tkinter import ttk

class InflationCalculator:
    def __init__(self, parent_frame):
        self.frame = ttk.LabelFrame(parent_frame, text="Inflationsrechner")
        self.frame.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="w")
        self.frame.grid_remove()

        initial_amount_label = ttk.Label(self.frame, text="Ursprungsbetrag (€):")
        initial_amount_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.initial_amount_entry = ttk.Entry(self.frame)
        self.initial_amount_entry.grid(row=0, column=1, padx=5, pady=5)

        inflation_rate_label = ttk.Label(self.frame, text="Inflationsrate (% pro Jahr):")
        inflation_rate_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.inflation_rate_entry = ttk.Entry(self.frame)
        self.inflation_rate_entry.grid(row=1, column=1, padx=5, pady=5)

        time_period_label = ttk.Label(self.frame, text="Zeitraum (Jahre):")
        time_period_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.time_period_entry = ttk.Entry(self.frame)
        self.time_period_entry.grid(row=2, column=1, padx=5, pady=5)

        calculate_button = ttk.Button(self.frame, text="Berechnen", command=self.calculate_inflation)
        calculate_button.grid(row=3, column=0, columnspan=2, pady=10)

        self.future_value_label = ttk.Label(self.frame, text="Zukünftiger Wert: ")
        self.future_value_label.grid(row=4, column=0, columnspan=2)

        self.purchasing_power_label = ttk.Label(self.frame, text="Kaufkraft (inflationsbereinigt): ")
        self.purchasing_power_label.grid(row=5, column=0, columnspan=2)

    def calculate_inflation(self):
        try:
            initial_amount = float(self.initial_amount_entry.get())
            inflation_rate = float(self.inflation_rate_entry.get()) / 100  # Convert percentage to decimal
            time_period = int(self.time_period_entry.get())
            
            future_value = initial_amount * (1 + inflation_rate) ** time_period
            purchasing_power = initial_amount / ((1 + inflation_rate) ** time_period)
            
            self.future_value_label.config(text=f"Zukünftiger Wert: {future_value:.2f} €")
            self.purchasing_power_label.config(text=f"Kaufkraft (inflationsbereinigt): {purchasing_power:.2f} €")
        except ValueError:
            self.future_value_label.config(text="Bitte gültige Zahlen eingeben")


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Inflationsrechner")
    app = InflationCalculator(root)
    root.mainloop()
