# Project Statement – Student Grade Manager

## Problem Statement

Teachers and class administrators often end up tracking student marks by hand. In notebooks, loose spreadsheets or scattered files. This makes it slow and error-prone to work out averages assign grades. See how the whole class is performing. There's no simple tool that just lets someone type in marks and immediately see the average, the grade and the class-wide picture.

Student Grade Manager solves this in the way possible: a command-line Python program where an administrator can add students record their marks and instantly get averages, grades and class statistics. Without needing spreadsheets or extra software.

## Objective

Let an administrator record a students name along with marks for one or more subjects.

Automatically calculate each students average. Convert it into a letter grade.

Allow marks to be updated or a student to be removed if needed.

Give a view of a single students report or the full list of students.

Show class-level statistics. The average lowest average and overall class average.

## Scope of the Project

### In scope:

A terminal-based menu that runs in a loop until the user chooses to exit.

Adding, updating, viewing and deleting student records for one session.

Calculating marks and assigning a grade (A+ to F) based on that average.

Showing class statistics across all added students.

### Out of scope (for this version):

Saving data to a file or database. All data is stored only in memory and is lost when the program closes.

A graphical or web interface. The project is command-line

User accounts, login or access control.

Input validation beyond what Python handles (e.g. the program does not check whether marks entered are within a valid range like 0–100).

Automated/unit testing. The project has been tested manually only.

## Target Users

Class administrators who want a quick no-fuss way to record marks and see grades for a small class or group, without setting up a spreadsheet or database.

Students learning Python who want an example of a menu-driven program that uses functions, dictionaries and multiple files working together.
