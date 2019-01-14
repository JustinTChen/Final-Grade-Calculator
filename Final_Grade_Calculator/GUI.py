from tkinter import *
import tkinter.messagebox

#CREATES WINDOW
root = Tk()

#Exit loop
def exit():
    root.destroy()

###############################################################################
"*** FRAMES ***"
##############################################################################
topFrame = Frame(root)
topFrame.pack(side=TOP, fill=BOTH)

midTopFrame = Frame(root, bg="light blue")
midTopFrame.pack(side=TOP, fill=BOTH)

bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM, fill=BOTH)

mainFrame = Frame(root, bg="light blue")
mainFrame.pack(side=RIGHT,fill=BOTH)

leftFrame = Frame(root, bg="light blue")
leftFrame.pack(side=LEFT, fill=BOTH)

##############################################################################
"*** TITLE ***"
##############################################################################
title = Label(topFrame, text='Grade Calculator',  bg="lavender", font="Georgia 12 bold", relief=SUNKEN)
title.pack(side=TOP, fill=X)

##############################################################################
"*** COURSE NAME INPUT ***"
##############################################################################
course_label = Label(midTopFrame, text="Course Name", bg="light blue", fg="purple", font="Georgia 18 bold")
course_entry = Entry(midTopFrame)
course_label.pack(side=LEFT)
course_entry.pack(fill=X)

##############################################################################
"*** LETTER GRADES ***"
##############################################################################
subTitle = Label(leftFrame, text="Cutoff Values for Letter Grades", bg="light blue", fg="purple", font="Georgia 14 bold")
subTitle.grid(columnspan=2)

class LetterGrade:
    def __init__(self, letter, number):
        self.letter = letter
        self.title = Label(leftFrame, text=letter, bg="light blue", fg="purple", font="Georgia 14")
        self.user_entry = Entry(leftFrame)
        self.title.grid(row=number+1)
        self.user_entry.grid(row=number+1, column=1)

A = LetterGrade("A/A+", 1)
A_minus = LetterGrade("A-", 2)
B_plus = LetterGrade("B-", 3)
B = LetterGrade("B", 4)
B_minus = LetterGrade("B-", 5)
passing = LetterGrade("passing", 6)

##############################################################################
"*** FINAL WORTH ***"
##############################################################################
final_label = Label(leftFrame, text="How much is the Final worth?", bg="light blue", fg="purple", font="Georgia 14 bold")
final_entry = Entry(leftFrame)
final_label.grid(row=8)
final_entry.grid(row=8, column=1)

##############################################################################
"*** GRADE COMPONENTS/MAIN BODY ***"
##############################################################################
header = Label(mainFrame, text="Grade Components", bg="light blue", fg="purple", font="Georgia 14 bold")
header.grid(columnspan=6)
instructions = Label(mainFrame, text="(Component is name of grade component (e.g. homework). Leave all numerical input in percentages, rounded to 2 dceimal points. If extra, leave blank.)", bg="light blue", fg="purple", font="Georgia 12")
instructions.grid(row=1, columnspan=6)

#component name entries
class Component:
    def __init__(self, number):
        self.title = Label(mainFrame, text="Grade Component", bg="light blue", fg="purple", font="Georgia 14")
        self.user_entry = Entry(mainFrame)
        self.title.grid(row=number+1)
        self.user_entry.grid(row=number+1, column=1)
component1 = Component(1)
component2 = Component(2)
component3 = Component(3)
component4 = Component(4)
component5 = Component(5)

#percentages entries
class Percentage:
    def __init__(self, number):
        self.title = Label(mainFrame, text="Percentage", bg="light blue", fg="purple", font="Georgia 14")
        self.user_entry = Entry(mainFrame)
        self.title.grid(row=number+1, column=2)
        self.user_entry.grid(row=number+1, column=3)
percentage1 = Percentage(1)
percentage2 = Percentage(2)
percentage3 = Percentage(3)
percentage4 = Percentage(4)
percentage5 = Percentage(5)

#grade entries
class Grade:
    def __init__(self, number):
        self.title = Label(mainFrame, text="Grade", bg="light blue", fg="purple", font="Georgia 14")
        self.user_entry = Entry(mainFrame)
        self.title.grid(row=number+1, column=4)
        self.user_entry.grid(row=number+1, column=5)
grade1 = Grade(1)
grade2 = Grade(2)
grade3 = Grade(3)
grade4 = Grade(4)
grade5 = Grade(5)

#CHECKBOX
c = Checkbutton(mainFrame, text="I do not have a 4.0", bg="light blue")
c.grid(columnspan=2)

##############################################################################
"*** Status Bar ***"
##############################################################################
class StatusBar(Frame):
    def __init__(self, master):
        self.string = StringVar()
        self.label = Label(bottomFrame, bd=1, relief=SUNKEN, anchor=W, textvariable=self.string)
        self.string.set("Calculating...")
        self.label.pack(side=BOTTOM, fill=X)

status = StatusBar(root)

#CALCULATE BUTTON
from Calculator import *
calculate = Button(mainFrame, text="Calculate", bg="light blue", fg="purple")
calculate.bind("<Button-1>", click)
calculate.grid(row=7, columnspan=6)

#Keeps command line running until user closes (essentially an infinite loop)
root.mainloop()
