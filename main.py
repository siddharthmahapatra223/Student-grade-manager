# this portion will run the code menu untill the function breaks
from operations import add, update, dlt
from view import viewstud, view_allstud
from grading import stat


def show():
    print("Student grade Manager")
    print("1 Add students")
    print("2 Update marks")
    print("3 View Students report")
    print("4 view all Students")
    print("5 Class Stats")
    print("6  Del student")
    print("7 exit")


def func():
    while True:
        show()
        c = input("Enter choice 1 to 7-")

        if c == "1":
            add()
        elif c == "2":
          update()
        elif c == "3":
          name = input("Enter name-")
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



func()
