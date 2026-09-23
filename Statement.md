#Project Statement – Student Grade Manager
##Problem Statement
Teachers and class administrators often end up tracking student marks by hand — in notebooks, loose spreadsheets, or scattered files. This makes it slow and error-prone to work out averages, assign grades, or see how the whole class is performing. There's no quick, simple tool that just lets someone type in marks and immediately see the average, the grade, and the class-wide picture.
Student Grade Manager solves this in the simplest way possible: a command-line Python program where an administrator can add students, record their marks, and instantly get averages, grades, and class statistics — without needing spreadsheets or extra software.
##Objective
Let an administrator record a student's name along with marks for one or more subjects.
Automatically calculate each student's average and convert it into a letter grade.
Allow marks to be updated or a student to be removed if needed.
Give a quick view of a single student's report or the full list of students.
Show class-level statistics — the highest average, lowest average, and overall class average.
##Scope of the Project
In scope:
A terminal-based menu that runs in a loop until the user chooses to exit.
Adding, updating, viewing, and deleting student records for one session.
Calculating average marks and assigning a grade (A+ to F) based on that average.
Showing basic class statistics across all added students.
Out of scope (for this version):
Saving data permanently to a file or database — all data is stored only in memory and is lost when the program closes.
A graphical or web interface — the project is command-line only.
User accounts, login, or access control.
Input validation beyond what Python naturally handles (e.g., the program does not check whether marks entered are within a valid range like 0–100).
Automated/unit testing — the project has been tested manually only.
##Target Users
Teachers or class administrators who want a quick, no-fuss way to record marks and see grades for a small class or group, without setting up a spreadsheet or database.
Students learning Python who want a simple example of a menu-driven program that uses functions, dictionaries, and multiple files working together.
