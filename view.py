#helps to view data
from store import stud
from grading import avg, grade
from operations import normal

def viewstud(name):
    name=normal(name)
    if name not in stud:
        print("Student not found\n")
        return

    marks = stud[name]
    av = avg(marks)
    gr = grade(av)

    print("-------", name, "-------")
    print("Marks:", marks)
    print("Average: %.2f" % av)
    print("Grade:", gr)
    print()

def view_allstud():
    if len(stud) == 0:
        print("No students added yet.\n")
        return

    print("\n--- All Students ---")
    for name in stud:
        print(name)
    print()
