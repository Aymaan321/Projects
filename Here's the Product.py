from tkinter import *

def calculate_product():
    try:
        num1 = int(entry1.get())
        num2 = int(entry2.get())
        product = num1 * num2
        result_box.delete("1.0", END)  # clear previous result
        result_box.insert(END, f"Product: {product}")
    except ValueError:
        result_box.delete("1.0", END)
        result_box.insert(END, "Please enter valid numbers.")

window = Tk()
window.geometry("400x300")
window.title("Getting Started with Widgets")


label1 = Label(window, text="Enter first number:")
label1.pack()
entry1 = Entry(window)
entry1.pack()

label2 = Label(window, text="Enter second number:")
label2.pack()
entry2 = Entry(window)
entry2.pack()

calc_button = Button(window, text="Calculate Product", command=calculate_product)
calc_button.pack(pady=10)

result_box = Text(window, height=2, width=30)
result_box.pack()

window.mainloop()
