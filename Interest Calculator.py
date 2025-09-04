import tkinter as tk
from tkinter import messagebox

def calculate_interest():
    try:
        original_amount = float(original_amount_entry.get())
        time = float(time_entry.get())
        rate = float(rate_entry.get())

        simple_interest = ((original_amount * time * rate) / 100) + original_amount

        compound_interest = original_amount * ((1 + (rate / 100)) ** time) 
        compound_interest = round(compound_interest, 2)

        result_label.config(
            text=f"Simple Interest: {simple_interest}\nCompound Interest: {compound_interest}"
        )
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numeric values.")

window = tk.Tk()
window.geometry("400x400")
window.title("Age(Interest) Calculator App")  

tk.Label(window, text="Original Amount:").grid(row=0, column=0, padx=10, pady=10, sticky="e")
original_amount_entry = tk.Entry(window)
original_amount_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(window, text="Time (years):").grid(row=1, column=0, padx=10, pady=10, sticky="e")
time_entry = tk.Entry(window)
time_entry.grid(row=1, column=1, padx=10, pady=10)

tk.Label(window, text="Rate of Interest (%):").grid(row=2, column=0, padx=10, pady=10, sticky="e")
rate_entry = tk.Entry(window)
rate_entry.grid(row=2, column=1, padx=10, pady=10)

calculate_button = tk.Button(window, text="Calculate", command=calculate_interest, bg='#82cfc7')
calculate_button.grid(row=3, columnspan=2, pady=20)

result_label = tk.Label(window, text="", font=("Bahnschrift", 12), fg="#182a47")
result_label.grid(row=4, columnspan=2, pady=20)

window.mainloop()

