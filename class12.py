import random
import tkinter as tk
from tkinter import messagebox


random_number = random.randint(1, 100)
tries = 0
max_tries = 5


def check_guess():
    global tries

    try:
        guessed_number = int(entry.get())
        tries += 1

        if guessed_number == random_number:
            result_label.config(
                text=f"🎉 Congratulations! You guessed it in {tries} tries.",
                fg="green"
            )
            guess_button.config(state="disabled")

        elif guessed_number > random_number:
            result_label.config(
                text=f"📉 Number is lower! Tries left: {max_tries - tries}",
                fg="blue"
            )

        else:
            result_label.config(
                text=f"📈 Number is higher! Tries left: {max_tries - tries}",
                fg="blue"
            )

  
        if tries >= max_tries and guessed_number != random_number:
            messagebox.showinfo(
                "Game Over",
                f"❌ Tries Over!\nThe number was {random_number}"
            )
            guess_button.config(state="disabled")

        entry.delete(0, tk.END)

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number!")


root = tk.Tk()
root.title("Number Guessing Game")
root.geometry("400x300")
root.config(bg="#1e1e2f")


title_label = tk.Label(
    root,
    text="🎮 Number Guessing Game",
    font=("Arial", 18, "bold"),
    bg="#1e1e2f",
    fg="white"
)
title_label.pack(pady=20)


instruction_label = tk.Label(
    root,
    text="Guess a number between 1 and 100",
    font=("Arial", 12),
    bg="#1e1e2f",
    fg="lightgray"
)
instruction_label.pack()


entry = tk.Entry(
    root,
    font=("Arial", 14),
    justify="center"
)
entry.pack(pady=15)


guess_button = tk.Button(
    root,
    text="Check Guess",
    font=("Arial", 12, "bold"),
    bg="#4CAF50",
    fg="white",
    padx=10,
    pady=5,
    command=check_guess
)
guess_button.pack()

result_label = tk.Label(
    root,
    text="",
    font=("Arial", 12),
    bg="#1e1e2f",
    fg="yellow"
)
result_label.pack(pady=20)


root.mainloop()


