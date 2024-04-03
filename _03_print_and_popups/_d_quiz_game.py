from tkinter import messagebox, simpledialog, Tk

# Create an if-main code block, *hint, type main then ctrl+space to auto-complete
    
    # Make a new window variable, window = Tk()
window = Tk()
    # Hide the window using the window's .withdraw() method
window.withdraw()
    # 1. Create a variable to hold the user's score. Set it equal to zero. 
score = 0
    # ASK A QUESTION AND CHECK THE ANSWER

    #      // 2.  Ask the user a question 
question = simpledialog.askstring(title = "Question #1", prompt = "What is 1+1?")
    #      // 3.  Use an if statement to check if their answer is correct
if int(question) == 2:
    score = score + 1
else:
    score = score - 1
    #      // 4.  if the user's answer was correct, add one to their score 
 
    # MAKE MORE QUESTIONS. Ask more questions by repeating the above 
    #      // Option: Subtract a point from their score for a wrong answer
question_2 = simpledialog.askstring(title = "Question #2", prompt = "What is my favorite color?")
if str(question_2) == "blue":
    score = score + 1
else:
    score = score - 1
question_3 = simpledialog.askstring(title = "Question #3", prompt = "What is the best food?")
if str(question_3) == "waffles":
    score = score + 1
else:
    score = score - 1
question_4 = simpledialog.askstring(title = "Question 4", prompt = "What is the square root of 16?")
if int(question_4) == 4:
    score = score + 1
else:
    score = score - 1
question_5 = simpledialog.askstring(title = "Question 5", prompt = "What is one thing you should do when you wake up and before you go to sleep?")
if str(question_5) = "brush teeth":
    score = score + 1
else:
    score = score - 1
    # After all the questions have been asked, tell the user their final score
messagebox.showinfo(title = "Final Score", message = str(score))
    # remember to convert your variable to a string using the str() function 
    
    # Run the window's .mainloop() method
