from tkinter import *
from datetime import date

def calculate_age():
    try:
        name = name_entry.get()
        day = int(day_entry.get())
        month = int(month_entry.get())
        year = int(year_entry.get())
        
        today = date.today()
        age = today.year - year - ((today.month, today.day) < (month, day))
        
        result_label.config(
            text=f"Hello {name}, you are {age} years old!",
            fg="blue"
        )
    except ValueError:
        result_label.config(text="Please enter valid values.", fg="red")

window = Tk()
window.geometry("400x400")
window.title("Age Calculator App")
window.configure(bg="#f0f8ff") 

Label(window, text="Name:", bg="#f0f8ff").grid(row=0, column=0, padx=10, pady=10, sticky="w")
name_entry = Entry(window)
name_entry.grid(row=0, column=1, padx=10, pady=10)

Label(window, text="Day:", bg="#f0f8ff").grid(row=1, column=0, padx=10, pady=10, sticky="w")
day_entry = Entry(window)
day_entry.grid(row=1, column=1, padx=10, pady=10)

Label(window, text="Month:", bg="#f0f8ff").grid(row=2, column=0, padx=10, pady=10, sticky="w")
month_entry = Entry(window)
month_entry.grid(row=2, column=1, padx=10, pady=10)

Label(window, text="Year:", bg="#f0f8ff").grid(row=3, column=0, padx=10, pady=10, sticky="w")
year_entry = Entry(window)
year_entry.grid(row=3, column=1, padx=10, pady=10)

calc_button = Button(window, text="Calculate Age", command=calculate_age, bg="#add8e6")
calc_button.grid(row=4, column=0, columnspan=2, pady=20)

result_label = Label(window, text="", bg="#f0f8ff", font=("Arial", 12, "bold"))
result_label.grid(row=5, column=0, columnspan=2, pady=20)

window.mainloop()
