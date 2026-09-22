#this is the main file of the project

from operations import add, update, delete
from view import viewstud, view_allstud
from grading import classstat


def menu():
    print("------ Student Marks Manager ------")
    print("1. Add Student")
    print("2. Update Marks")
    print("3. View Student Report")
    print("4. View All Students")
    print("5. Class Statistics")
    print("6. Delete Student")
    print("7. Exit")


def main():
    while True:
        menu()
        c = input("Enter your choice (1-7): ")

        if c == "1":
            add()
        elif c == "2":
            update()
        elif c == "3":
            name = input("Enter student name: ")
            viewstud(name)
        elif c == "4":
            view_allstud()
        elif c == "5":
            classstat()
        elif c == "6":
            delete()
        elif c == "7":
            print("Bye!")
            break
        else:
            print("Invalid\n")


if __name__ == "__main__":
    main()
