import tkinter as tk

def check_strength():
    password = entry.get()
    length = len(password)

    if length <= 5:
        strength = "Weak"
        color = "red"
    elif 6 <= length <= 8:
        strength = "Medium"
        color = "yellow"
    elif 9 <= length <= 12:
        strength = "Strong"
        color = "light green"
    else:
        strength = "Very Strong"
        color = "dark green"

    result_label.config(text=f"Strength: {strength}", fg=color)

root = tk.Tk()
root.geometry("400x400")
root.title("Length Converter App")

instruction = tk.Label(root, text="Enter your password:", font=("Arial", 14))
instruction.pack(pady=20)

entry = tk.Entry(root, show="*", font=("Arial", 14), width=30)
entry.pack(pady=10)

check_button = tk.Button(root, text="Check Strength", command=check_strength, font=("Arial", 12), bg="#add8e6")
check_button.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.pack(pady=20)

root.mainloop()
