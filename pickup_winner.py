from tkinter import *
from PIL import ImageTk, Image
from random import randint

root = Tk()
root.title("Who is the winner?")
root.geometry("400x400")
root.resizable(False, False)


def pickup():
    entries = ['Candidate 1', 'Candidate 2', 'Candidate 1', 'Candidate 2', 'Candidate 3', 'Candidate 4', 'Candidate 5', 'Candidate 6', 'Candidate 7', 'Candidate 8', 'Candidate 9', 'Candidate 10', 'Candidate 11', 'Candidate 12', 'Candidate 13', 'Candidate 14', 'Candidate 15', 'Candidate 15', 'Candidate 16', 'Candidate 17', 'Candidate 18', 'Candidate 19', 'Candidate 20', 'Candidate 21', 'Candidate 22', 'Candidate 23', 'Candidate 21', 'Candidate 24', 'Candidate 25', 'Candidate 26', 'Candidate 27', 'Candidate 28', 'Candidate 29', 'Candidate 30']
    entries_set = set(entries)
    unique_entries = list(entries_set) # unsorted

    random_num = randint(0, len(unique_entries)-1)

    global winner_label
    winner_label.grid_forget()
    winner_label = Label(root, text=unique_entries[random_num], font=("Helvtica", 16))
    winner_label.grid(row = 2, column = 0, padx=100, pady=10)

topLabel = Label(root, text="Win-O-Rama", font=("Helvtica", 20, "bold"))
topLabel.grid(row = 0, column = 0, padx=100, pady=(20,10))

btn = Button(root, text="Pickup a winner", font=("Helvtica", 14), command=pickup)
btn.grid(row = 1, column = 0, padx=100, pady=10)

winner_label = Label(root, text="", font=("Helvtica", 16))
winner_label.grid(row = 2, column = 0, padx=100, pady=10)


root.mainloop()
