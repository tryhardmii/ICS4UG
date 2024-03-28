from tkinter import *
import sys


window = Tk()
global n
n = 0

global answers
answers = 0
personality_type = []
questions = [
    "1. I feel more energized and refreshed after being around other people.",
    "2. I am more comfortable in large social gatherings with many people.",
    "3. When faced with a new situation or challenge, I prefer to work through it with the support and input of others.",
    "4. When approaching networking or building new relationships, I actively seek out new connections rather than forming deeper bonds with a smaller circle of friends.",
    "5. When recharging after a long day, I prefer to be around people.",
    "6. When making decisions, I tend to rely more on gut instincts and hunches.",
    "7. In new or unfamiliar situations I am more drawn to exploring possibilities and potential outcomes.",
    "8. When approaching problem-solving, you trust your intuition to guide you toward solutions.",
    "9. When learning something new, I prefer to dive in and experiment.",
    "10. I pick up on underlying patterns and meanings easily.",
    "11. When faced with a tough decision, I prioritize how my choices will impact others and their emotions.",
    "12. When expressing my opinions and beliefs do you rely on your personal values and emotions to guide your arguments.",
    "13. When providing feedback to others, I consider how my words will affect their feelings and emotional well-being.",
    "14. When solving interpersonal conflicts I emphasize empathy and understanding to find common ground.",
    "15. In my decision-making process, I give more weight to my gut feelings and instincts.",
    "16. When planning a trip or project, I feel more comfortable having a clear, organized itinerary or timeline to follow.",
    "17. When approaching deadlines and goals, I prefer to set specific deadlines and stick to a structured plan to achieve my objectives.",
    "18. I prefer to have a sense of predictability and stability in my life.",
    "19. I prefer to make decisions quickly and move forward with a clear plan of action",
    "20. In my daily life, I carefully plan and organize my activities to maximize efficiency and productivity."
]
label1 = Label(window, text = questions[n], font = ("Arial"))
entry1 = Entry(window, width = 10)
def one():
    global n, label1, answers
    n += 1
    if n < len(questions):
        label1.configure(text=questions[n] + "\n1. Strongly Disagree\n2. Disagree\n3. Neutral\n4. Agree\n5. Strongly Agree")
    answers += 1
    personality()
def two():
    global n, label1, answers
    n += 1
    if n < len(questions):
        label1.configure(text=questions[n] + "\n1. Strongly Disagree\n2. Disagree\n3. Neutral\n4. Agree\n5. Strongly Agree")
    answers += 2
    personality()
def three():
    global n, label1, answers
    n += 1
    if n < len(questions):
        label1.configure(text=questions[n] + "\n1. Strongly Disagree\n2. Disagree\n3. Neutral\n4. Agree\n5. Strongly Agree")
    answers += 3
    personality()
def four():
    global n, label1, answers
    n += 1
    if n < len(questions):
        label1.configure(text=questions[n] + "\n1. Strongly Disagree\n2. Disagree\n3. Neutral\n4. Agree\n5. Strongly Agree")
    answers += 4
    personality()
def five():
    global n, label1, answers
    n += 1
    if n < len(questions):
        label1.configure(text=questions[n] + "\n1. Strongly Disagree\n2. Disagree\n3. Neutral\n4. Agree\n5. Strongly Agree")
    answers += 5
    personality()

def getage():
    global entry1
    userinput = entry1.get()
    with open("responses.txt", "a") as f:
        f.write(userinput + "/")
    backtomenu()

def giveage():
    global entry1
    clear_screen()
    label1 = Label(window, text = "Enter age: ")
    entry1 = Entry(window, width = 10)
    label1.grid(row = 0, column = 0)
    entry1.grid(row = 0, column = 1)
    button2 = Button(window, text = "Enter", command = getage)
    button2.grid(row = 0, column = 2)

def personality():
    global answers, personality_type, questions
    if n == 5:
        if answers > 15:
            personality_type.append("E") #extrovert
            answers = 0
        else:
            personality_type.append("I") #introvert
            answers = 0
    elif n == 10:
        if answers > 15:
            personality_type.append("N") #intuitive
            answers = 0
        else:
            personality_type.append("S") #observant
            answers = 0
    elif n == 15:
        if answers > 15:
            personality_type.append("F") #feeling
            answers = 0
        else:
            personality_type.append("T") #thinking
            answers = 0
    elif n == 20:
        if answers > 15:
            personality_type.append("J") #judging
            answers = 0
        else:
            personality_type.append("P") #prospecting
            answers = 0
    else:
        if n > 20:
            with open("responses.txt", "a") as f:
                f.write(personality_type[0] + "/" + personality_type[1] + "/"
            + personality_type[2] + "/" + personality_type[3] + "/")
                giveage()
                pass
def answer_questions():
    global n, label1
    clear_screen()
    if n < len(questions):
        label1 = Label(window, text=questions[n], font=("Arial"))
    else:
        backtomenu()
    button1 = Button(window, text="1", font=("Arial"), command=one)
    button2 = Button(window, text="2", font=("Arial"), command=two)
    button3 = Button(window, text="3", font=("Arial"), command=three)
    button4 = Button(window, text="4", font=("Arial"), command=four)
    button5 = Button(window, text="5", font=("Arial"), command=five)
    label11 = Label(window, text="1. Strongly Disagree", font=("Arial"))
    label2 = Label(window, text="2. Disagree", font=("Arial"))
    label3 = Label(window, text="3. Neutral", font=("Arial"))
    label4 = Label(window, text="4. Agree", font=("Arial"))
    label5 = Label(window, text="5. Strongly Agree", font=("Arial"))
    label1.grid(row=0, column=0)
    button1.grid(row=2, column=0)
    label11.grid(row=2, column=1)
    button2.grid(row=3, column=0)
    label2.grid(row=3, column=1)
    button3.grid(row=4, column=0)
    label3.grid(row=4, column=1)
    button4.grid(row=5, column=0)
    label4.grid(row=5, column=1)
    button5.grid(row=6, column=0)
    label5.grid(row=6, column=1)
def getinputtext():
    global entry1
    userinput = entry1.get()
    with open("responses.txt", "a") as f:
        f.write(userinput + "/")
    answer_questions()
    pass
def backtomenu():
    clear_screen()
    main_menu()
def clear_screen():
    for widget in window.winfo_children():
        widget.destroy()
def exit():
    sys.exit()
def name_user():
    global n, label1, entry1
    clear_screen()
    label1 = Label(window, text = "enter name", font = ("Arial"))
    entry1 = Entry(window, font = ("Arial"))
    button = Button(window, text = "Enter", font = ("Arial"), command = getinputtext)
    label1.grid(row = 0, column = 0)
    entry1.grid(row = 1, column = 0)
    button.grid(row = 1, column = 1)
def next_question():
    global n, label1
    label1.configure(text=questions[n])
    n += 1
def compatibility(self, other):
  compatibility = 0
  common = 0
  self = self.split("/")
  other = other.split("/")
  if self[1] == other[1]:
    compatibility += 7
    common += 1
  if self[2] == other[2]:
    compatibility += 3
    common += 1
  if self[3] == other[3]:
    compatibility += 3
    common += 1
  if self[4] == other[4]:
    compatibility += 3
    common += 1
  compatibility += (common**2) * 2
  compatibility -= abs((int(self[5]) - int(other[5])) / 2)
  if compatibility < 0:
      return 0
  else:
      return compatibility
def seeusermatches():
    global entry1, matchvalues
    userinput = int(entry1.get())
    clear_screen()
    label1 = Label(window, text = matchvalues[userinput], font = ("Arial"))
    label1.pack()
    back_button = Button(window, text = "Back", font = ("Arial"), command = backtomenu)
    back_button.pack()
def match_users():
    clear_screen()
    global matchvalues, entry1
    listofmatches = []
    matchvalues = []
    personmatches = []
    with open("responses.txt", "r") as f:
        lines = f.readlines()
        for i in range(len(lines)):
            listofmatches.append(lines[i].replace("\n", "").split("/"))
        print(listofmatches)
        compatibility(lines[0], lines[1])
    for i in range(len(listofmatches)):
        personmatches = [compatibility(lines[i], lines[n]) if n != i else "x" for n in range(len(listofmatches))]
        matchvalues.append(personmatches)
    print(matchvalues)
    for i in range(len(matchvalues) + 1):
        for j in range(len(matchvalues) + 1):
            frame = Frame(window, relief=RAISED, borderwidth=1, width=100, height=100)
            frame.grid(row=i, column=j)
            if i == 0 and j == 0:
                display = Label(frame, text="%10s" % "Names", font = ("Arial"))
                display.pack()
            elif i == 0 and j != 0:
                display = Label(frame, text="%10s" % listofmatches[j - 1][0], font=("Arial"))
                display.pack()
            elif i != 0 and j == 0:
                display = Label(frame, text="%10s" % listofmatches[i - 1][0], font=("Arial"))
                display.pack()
            else:
                display = Label(frame, text="%10s" % matchvalues[i - 1][j - 1])
                display.pack()
    labela = Label(window, text= "Match Values (higher is better)", font=("Arial"))
    labela.grid(row=len(matchvalues) + 2, column = len(matchvalues) + 2)
    back = Button(window, text="Back", command = backtomenu, font = ("Arial"))
    quit = Button(window, text="Exit", command = exit)
    back.grid(row=len(matchvalues), column = len(matchvalues) + 2)
    quit.grid(row=len(matchvalues) + 1, column=len(matchvalues) + 2)
def main_menu():
    clear_screen()
    title = Label(window, text = "Dating app", font = 'Helvetica 50 bold', fg = 'red', bg = 'blue')
    button1 = Button(window, text = "1. Create new user", command = name_user)
    button2 = Button(window, text = "2. Match users", command = match_users)
    button3 = Button(window, text = "3. Quit", command = exit)

    title.pack()
    button1.pack()
    button2.pack()
    button3.pack()


main_menu()

window.mainloop()






























