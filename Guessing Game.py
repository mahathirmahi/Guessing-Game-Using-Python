import tkinter as tk
from tkinter import messagebox
import random

class GuessingGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Guessing Game")
        
        self.secret_number = random.randint(1, 100)
        self.guesses_remaining = 5

        self.label = tk.Label(self.master, text="Guess a number between 1 and 100:")
        self.label.pack()

        self.entry = tk.Entry(self.master)
        self.entry.pack()

        self.submit_button = tk.Button(self.master, text="Submit Guess", command=self.check_guess)
        self.submit_button.pack()

    def check_guess(self):
        try:
            guess = int(self.entry.get())
            self.guesses_remaining -= 1

            if guess == self.secret_number:
                messagebox.showinfo("Congratulations!", f"You guessed the number {self.secret_number} correctly!")
                self.master.destroy()
            elif guess < self.secret_number:
                messagebox.showinfo("Incorrect", "Try a higher number.")
            else:
                messagebox.showinfo("Incorrect", "Try a lower number.")

            if self.guesses_remaining == 0:
                messagebox.showinfo("Game Over", f"You've run out of guesses. The correct number was {self.secret_number}.")
                self.master.destroy()
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number.")

# Create the main window
root = tk.Tk()

# Initialize the game
game = GuessingGame(root)

# Run the main loop
root.mainloop()
