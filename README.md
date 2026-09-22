# Student Grade Manager

A simple command-line program written in Python that helps a teacher or admin keep track of students, their marks, and their grades — all from the terminal, no extra software needed.

## Overview

Keeping a class's marks on paper or in scattered files gets messy fast. This project gives a small, no-frills tool where you can type in a student's name and marks, and the program instantly works out their average and letter grade. You can also update marks later, remove a student, or check how the whole class is doing at a glance.

It's built as a personal/academic project to practice core Python concepts — dictionaries, functions, loops, and splitting code into separate files — rather than as a production-ready system.

## Features

- **Add a student** – enter a name and marks for as many subjects as you like.
- **Update marks** – re-enter a student's subject marks if they change.
- **View one student's report** – see their marks, average, and grade.
- **View all students** – get a quick list of every student added so far.
- **Class statistics** – see the highest average, lowest average, and the class average in one go.
- **Delete a student** – remove a student's record completely.
- Simple text menu that keeps running until you choose to exit.

## Tech Stack

- **Language:** Python 3 (standard library only — no external packages needed)
- **Interface:** Command line / terminal
- **Storage:** In-memory Python dictionary (data is not saved to a file, so it resets every time the program restarts)

## Project Structure

```
Student-grade-manager/
├── main.py          # Menu loop – the entry point of the program
├── operations.py    # Add, update, and delete student records
├── view.py          # Show one student's report or the full student list
├── grading.py       # Calculates average, grade, and class-wide stats
├── store.py         # Holds the shared dictionary where student data lives
└── README.md
```

## How It Works

- Every student is stored as an entry in a dictionary, where the name is the key and the list of marks is the value.
- The `grading.py` file turns a list of marks into an average, and that average into a letter grade using this scale:

| Average Marks | Grade |
|---|---|
| 90 and above | A+ |
| 80 – 89 | A |
| 70 – 79 | B |
| 60 – 69 | C |
| 50 – 59 | D |
| Below 50 | F |

## Setup Instructions

1. Make sure Python 3 is installed on your computer.
2. Download or clone this repository:
   ```
   git clone https://github.com/siddharthmahapatra223/Student-grade-manager.git
   ```
3. Move into the project folder:
   ```
   cd Student-grade-manager
   ```
4. Run the program:
   ```
   python main.py
   ```

## Usage

When you run the program, you'll see a menu like this:

```
Student grade Manager
1 Add students
2 Update marks
3 View Students report
4 view all Students
5 Class Stats
6 Del student
7 exit
```

Just type the number of what you want to do and follow the prompts. For example, choosing **1** will ask for a student's name and their marks subject by subject, then save the record.

## Known Limitations

- Data isn't saved anywhere — closing the program clears everything.
- The program doesn't check if the marks you type in are valid numbers within a sensible range, so an unexpected entry (like text instead of a number) can cause an error.
- No login or access control — anyone running the program can add, change, or delete records.
- No automated tests included; the program has only been tested manually.

## Future Improvements

- Save student records to a file or database so data isn't lost on exit.
- Add input validation so the program doesn't crash on bad input.
- Add a way to edit a single subject's mark instead of re-entering all of them.
- Write some basic tests to check that the grading logic works correctly.

## Contributing

This is a small academic project, but suggestions are welcome:

1. Fork the repository.
2. Create a new branch for your change.
3. Make your changes and test them manually.
4. Open a pull request describing what you changed and why.

## Author

Siddharth Mahapatra
