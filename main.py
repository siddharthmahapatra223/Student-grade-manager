# this portion will run the code
from operations import add, update, dlt
from view import viewstud, view_allstud
from grading import stat


def show():
    print("Student Marks Manager")
    print("1 Add students")
    print("2 Update marks")
    print("3 View Student report")
    print("4 view all Students")
    print("5 Class Statistics")
    print("6  Del student")
    print("7 exit")


def main():
    while True:
        show()
        c = input("Enter choice 1 to 7")

        if c == "1":
            add()
        elif c == "2":
          update()
        elif c == "3":
          name = input("Enter student name")
          viewstud(name)
        elif c == "4":
          view_allstud()
        elif c == "5":
           stat()
        elif c == "6":
          dlt()
        elif c == "7":
            print("end")
            break
        else:
            print("invalid")
            print()



main()
