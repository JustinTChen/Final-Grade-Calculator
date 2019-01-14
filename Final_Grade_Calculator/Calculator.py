from GUI import *
from datascience import *
import numpy as np

bins = [A, A_minus, B_plus, B, B_minus, passing]
raw_data = [[component1, percentage1, grade1],
            [component2, percentage2, grade2],
            [component3, percentage3, grade3],
            [component4, percentage4, grade4],
            [component5, percentage5, grade5]]

def arrays():
    copy = raw_data[:]
    component, percentage, grade_array, raw = make_array(), make_array(), make_array(), make_array()
    current = copy[0]
    while current and (current[0].user_entry.get() != "") and (current[1].user_entry.get() != "") and (current[2].user_entry.get() != ""):
        c, p, g = current[0].user_entry.get(), int(current[1].user_entry.get()), float(current[2].user_entry.get())
        component, percentage = np.append(component, c), np.append(percentage, p)
        grade_array, raw = np.append(grade_array, g), np.append(raw, g * (p / 100))
        copy = copy[1:]
        current = copy[0]
    return [component, percentage, grade_array, raw]

def make_table(lst_arrays):
    return Table().with_columns("Component", lst_arrays[0],
                                 "Percentage", lst_arrays[1],
                                 "Grade", lst_arrays[2],
                                 "Raw Score", lst_arrays[3])



def calculator(final, grade_needed, summary):
    final = int(final_entry.get())
    raw_final = float(grade_needed) - sum(summary.column("Raw Score"))
    needed = raw_final / (final / 100)
    return needed

def display(summary, bins):
    final = int(final_entry.get())
    course_name, content = "Final Exam Calculator for " + course_entry.get(), ""
    for bin in bins:
        output = calculator(final, bin.user_entry.get(), summary)
        if output > 100:
            content += "For a {0} grade, you need a {1}% on the final. Not possible unless there is extra credit!".format(bin.letter, round(output, 2)) + "\n" + "\n"
        elif output < 0:
            content += "For a {0} grade, you good. Automatic!".format(bin.letter, round(output, 2)) + "\n" + "\n"
        else:
            content += "For a {0} grade, you need a {1}% on the final.".format(bin.letter, round(output, 2)) + "\n" + "\n"
    tkinter.messagebox.showinfo(title=course_name, message=content)

def click(event):
    summary = make_table(arrays())
    return display(summary, bins)
