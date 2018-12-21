from datascience import *
import numpy as np

#Initializes
def start():
    print("Welcome to your grade calculator")
    return helper()

#Returns arrays for each component of a course
def helper():
    component, percentage, grade_array, raw = make_array(), make_array(), make_array(), make_array()
    part = input("Enter grade component followed by percentage, separated by a comma. If finished, enter done: ").lower()
    while part != "done":
        grade = input("What is your grade for this component (leave exact)? ")
        split = part.split(",")
        cleaned = [n.replace(" ","") for n in split]
        component, percentage = np.append(component, cleaned[0]), np.append(percentage, cleaned[1])
        grade_array, raw = np.append(grade_array, float(grade)), np.append(raw, float(grade) * (int(cleaned[1]) / 100))
        part = input("Enter grade component followed by percentage, separated by a comma. If finished, enter done: ").lower()
    return [component, percentage, grade_array, raw]

#Can change
def what_grade():
    grade_needed = input("What overall course grade percentage do you need for the desired letter grade? ")
    return grade_needed

#Calculates the final grade needed for a given overall course grade
def calculator(final, grade_needed, summary):
    print("Calculating...")
    raw_final = float(grade_needed) - sum(summary.column("Raw Score"))
    needed = raw_final / (int(final) / 100)
    return needed

#Display the result
def display(summary, action=False):
    global grade_needed
    if action:
        grade_needed = what_grade()
        output = calculator(final, grade_needed, summary)
    else:
        output = calculator(final, grade_needed, summary)
    if output > 100:
        print("For a {0}, you need a {1}% on the final. Not possible unless there is extra credit!".format(grade_needed, output))
    else:
        print("For a {0}, you need a {1}% on the final.".format(grade_needed, output))

#Allow chance to change inputs to recalculate
def change():
    status = input("Would you like to make any changes (y/n)? ")
    if status == "y":
        return True
    return False

#Ask for changes
def changes():
    global summary
    want_change = change()
    #Action based on change status
    while want_change:
        response = input("Do you want to change the letter grade desired or a component grade (letter/component)? ").lower()
        if response == "letter":
            display(summary, True)
        elif response == "component":
            which = input("Which one? Please choose from the following" + str(list(summary.column("Component"))) + ": ").lower()
            try:
                maybe = array_remove(which)
                new_val = float(input("New {0} grade: ".format(which)))
                arrays = [summary.column(n) for n in range(len(summary))]
                arrays[0], arrays[1] = np.append(arrays[0], which), np.append(arrays[1], maybe)
                arrays[2], arrays[3] = np.append(arrays[2], new_val), np.append(arrays[3], new_val * (int(maybe) / 100))
                new_summary = make_table(arrays)
                display(new_summary)
            except:
                print("Invalid component name. Please try again.")
        else:
            print("Please enter the word grade or component")
        want_change = change()
    print("Ok. Goodbye and Good Luck!")

def array_remove(row_attr):
    assert row_attr in summary.column("Component")
    n = 0
    for row in summary.rows:
        if row.item("Component") == row_attr:
            keep = row.item("Percentage")
            summary.remove(n)
            return keep
        n += 1

def make_table(lst_arrays):
    return Table().with_columns("Component", lst_arrays[0],
                                 "Percentage", lst_arrays[1],
                                 "Grade", lst_arrays[2],
                                 "Raw Score", lst_arrays[3])

##############################################################################
"*** START THE PROGRAM ***"
##############################################################################
course = input("What course is this for? ")
#Mutable list of component grades
arrays = start()
#Keeps track of original to reset, if needed
reset = arrays
#Puts course grade information into a table from an array
summary = make_table(arrays)
#SHOULD NOT CHANGE
final = input("How much percent is the final worth? ")
#Can change
grade_needed = what_grade()
#Call
display(summary)
##############################################################################
"*** CHANGING ELEMENTS OPTION ***"
##############################################################################
#Allow option to change info
changes()
