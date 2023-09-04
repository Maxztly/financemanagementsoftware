import tkinter as tk
from tkinter import ttk

class RentalYieldCalculator:
    def __init__(self, parent_frame):
        self.frame = ttk.LabelFrame(parent_frame, text="Mietrendite-Rechner")
        self.frame.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="w")
        self.frame.grid_remove()

        purchase_price_label = ttk.Label(self.frame, text="Kaufpreis der Immobilie (€):")
        purchase_price_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.purchase_price_entry = ttk.Entry(self.frame)
        self.purchase_price_entry.grid(row=0, column=1, padx=5, pady=5)

        monthly_rent_label = ttk.Label(self.frame, text="Monatliche Mieteinnahmen (€):")
        monthly_rent_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.monthly_rent_entry = ttk.Entry(self.frame)
        self.monthly_rent_entry.grid(row=1, column=1, padx=5, pady=5)

        calculate_button = ttk.Button(self.frame, text="Berechnen", command=self.calculate_rental_yield)
        calculate_button.grid(row=2, column=0, columnspan=2, pady=10)

        self.result_label = ttk.Label(self.frame, text="Mietrendite (jährlich): ")
        self.result_label.grid(row=3, column=0, columnspan=2)

        self.monthly_yield_label = ttk.Label(self.frame, text="Mietrendite (monatlich): ")
        self.monthly_yield_label.grid(row=4, column=0, columnspan=2)

    def calculate_rental_yield(self):
        try:
            purchase_price = float(self.purchase_price_entry.get())
            monthly_rent = float(self.monthly_rent_entry.get())
            
            annual_rent = monthly_rent * 12
            rental_yield = (annual_rent / purchase_price) * 100
            monthly_yield = rental_yield / 12
            
            self.result_label.config(text=f"Mietrendite (y): {rental_yield:.2f}%")
            self.monthly_yield_label.config(text=f"Mietrendite (m): {monthly_yield:.2f}%")
        except ValueError:
            self.result_label.config(text="Bitte gültige Zahlen eingeben")


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Mietrendite-Rechner")
    app = RentalYieldCalculator(root)
    root.mainloop()
