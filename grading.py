#this file contains the functions to calc avg, grade and class stats
from store import stud


def avg(marks):
    if len(marks)!=0:
      s = 0
      for m in marks:
          s += m
      return s / len(marks)
        
    else:
        print("no data available")

def grade(average):
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"


def stat():
    if len(stud) == 0:
        print("No students added yet.\n")
        return

    allavg = [avg(marks) for marks in stud.values()]
    high = max(allavg)
    low = min(allavg)
    classavg = sum(allavg) / len(allavg)
    print("highest:", high, "\nlowest:", low, "\nClass average:", classavg,"\n")
