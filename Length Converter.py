from tkinter import *

def convert():
    try:
        in_value = float(entry1.get())
        cm_value = in_value * 2.54
        cm_value = round(cm_value, 1)
        result_box.delete("1.0", END)  
        result_box.insert(END, f"cm Value: {cm_value}")
    except ValueError:
        result_box.delete("1.0", END)
        result_box.insert(END, "Please enter valid numbers.")
    
window = Tk()
window.geometry('400x400')
window.title('Length Converter App')

label1 = Label(window, text="Enter inches value:")
label1.pack()
entry1 = Entry(window)
entry1.pack()

calc_button = Button(window, text="Convert", command=convert)
calc_button.pack(pady=10)

result_box = Text(window, height=2, width=30)
result_box.pack()

window.mainloop()
