#this includes all the operations that can be done on the stud dict

from store import stud
from grading import avg, grade

def normal(name):
    return name.strip().title()

def add():
    name = normal(input("Enter student's name: "))

    if name in stud:
        print(name, "exists\n")
        return

    marks = []
    numsub = int(input("Enter the no. of subjects: "))
    while numsub < 1:
       print("Must enter at least 1 subject.")
       numsub = int(input("Enter the no. of subjects: "))
    for i in range(numsub):
        mark = float(input(f"Enter the marks for subject {i+1}: "))
        marks.append(mark)

    stud[name] = marks
    print(name, "added.\n")


def update():
    name = normal(input("Enter the student's name: "))
    if name not in stud:
        print("Student not found\n")
        return

    marks = []
    numsubjects = int(input("Enter no. of subjects: "))
    for i in range(numsubjects):
        mark = float(input(f"Enter the marks for subject {i+1}: "))
        marks.append(mark)

    stud[name] = marks
    print("updated\n")



def dlt():
    name = normal(input("Enter student name to delete: "))
    if name in stud:
        del stud[name]
        print(name, "deleted\n")
    else:
        print("Student not found\n")
