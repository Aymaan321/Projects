import tkinter as tk
from tkinter import messagebox
import random

root = tk.Tk()
root.title('Rock Paper Scissors App')
root.geometry('400x400')

rps = ['rock', 'paper', 'scissors']

def comp_choice():
    return random.choice(rps)

def play_game():
    user = entry.get().lower()
    comp = comp_choice() 

    if user not in rps:
        messagebox.showerror('Wrong Input', 'Please enter rock, paper or scissors.')
        return

    if user == comp:
        messagebox.showinfo('Result', f'Computer chose {comp}. It was a draw!')
    elif (user == 'rock' and comp == 'scissors') or \
         (user == 'paper' and comp == 'rock') or \
         (user == 'scissors' and comp == 'paper'):
        messagebox.showinfo('Result', f'Computer chose {comp}. You won!')
    else:
        messagebox.showinfo('Result', f'Computer chose {comp}. You lost!')

    lbl2.config(text=f"Computer's last choice: {comp}")

lbl1 = tk.Label(root, text='Please enter your choice:\nRock, Paper, Scissors', padx=20, pady=20)
lbl2 = tk.Label(root, text="Computer's last choice: None", padx=20, pady=20)
entry = tk.Entry(root)
btn1 = tk.Button(root, text='Play', command=play_game)

lbl1.pack()
entry.pack()
btn1.pack()
lbl2.pack()

root.mainloop()
