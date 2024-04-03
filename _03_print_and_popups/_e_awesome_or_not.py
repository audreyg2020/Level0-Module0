from tkinter import messagebox, simpledialog, Tk
import random

# Create an if-main code block, *hint, type main then ctrl+space to auto-complete
if __name__ == '__main__':

    # Make a new window variable, window = Tk()
    window = Tk()
    # Hide the window using the window's .withdraw() method
    window.withdraw()
    # 1. Make a variable equal to a positive number less than 4 using random.randInt(0, 3)
number_less_than_four = random.randint(0,3)
    # 2. Print your variable to the console
print()
    # 3. Get the user to enter something that they think is awesome
something_awesome = simpledialog.askstring(title = "Enter Reponse", prompt = "What do you think is something awesome?")
    # 4. If your variable is  0
        # -- tell the user whatever they entered is awesome!
if number_less_than_four == 0:
    messagebox.showinfo(title = "Evaluation", message = something_awesome + " is awesome!")
    # 5. If your variable is  1
        # -- tell the user whatever they entered is ok.
if number_less_than_four == 1:
    messagebox.showinfo(title = "Evaluation", message = something_awesome + " is ok.")
    # 6. If your variable is  2
        # -- tell the user whatever they entered is boring.
if number_less_than_four == 2:
    messagebox.showinfo(title = "Evaluation", message = something_awesome + " is boring.")
    # 7. If your variable is  3
        # -- invent your own message to give to the user (be nice).
if number_less_than_four == 3:
    messagebox.showinfo(title = "Evaluation", message = something_awesome + " is cool, but it could definitely be more awesome.")
    # Run the window's .mainloop() method
window.mainloop()
