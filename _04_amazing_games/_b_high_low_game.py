from tkinter import messagebox, simpledialog, Tk
import sys
import random

if __name__ == '__main__':
    window = Tk()
window.withdraw()

    # 1. Change this line to give you a random number between 1 - 100.
random_num = random.randint(1, 10)

    # 2. Print out the random variable that you made in step #1
print()
    # 3. Code a for loop to run steps 4-10, 10 times
correct = 0
for steps_4_to_10 in range(10):
        # 4. Ask the user for a guess using a pop-up window, and save their response
    guess = simpledialog.askstring(title = "Enter a Response", prompt = "Guess a number between 1 and 10")
        # 5. If the guess is correct
    if int(guess) == random_num:
        sys.exit()
            # 6. Win. Use 'sys.exit(0)' to end the program
    if int(guess) > random_num:
        messagebox.showinfo(title = "How'd you do?", message = "Your guess was too high!")
        # 7. if the guess is high
            # 8. Tell them it's too high
    else:
        messagebox.showinfo(title = "How'd you do?", message = "Your guess was too low!")
        # 9. Else if the guess is low
            # 10. Tell them it's too low

    #11. Outside of the loop, tell the user they lost
messagebox.showinfo(title = "Final Result", message = "You lost.")
window.mainloop()
