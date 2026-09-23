# Student Grade Manager

A simple command-line program written in Python that helps a teacher or administrator keep track of students their marks and their grades. From the terminal without any extra software.

## Overview

I found that keeping a classs marks on paper or in scattered files can become messy quickly. This project offers a no-frills tool where you can type a students name and marks and the program immediately calculates the average and letter grade. You can also update marks later delete a student or see how the entire class is performing at a glance.

I built this project as an academic exercise to practice core Python concepts such as dictionaries, functions, loops and dividing code into separate files rather than as a production-ready solution.

## Features

- **Add a student** – provide a name and marks for any number of subjects you wish.

- **Update marks** – re-enter a students subject marks when they change.

- **View one students report** – view their marks, grade.

- **View all students** – obtain a list of every student added to date.

- **Class statistics** – view the average, the lowest average and the overall class average all at once.

- **Delete a student** – remove a students record entirely.

- A simple text menu that continues to run until you decide to exit.

## Tech Stack

- **Language:** Python 3 ( standard library, no external packages required)

- **Interface:** Command line or terminal

- **Storage:** In-memory Python dictionary (data is not written to a file so it resets each time the program restarts)

## Project Structure

```

Student-grade-manager/

|--- main.py          # Menu loop – the entry point of the program

|--- operations.py    # Add, update and delete student records

|--- view.py          # Show one students report or the full student list

|--- grading.py       # Calculates average, grade and class-wide stats

|--- store.py         # Holds the shared dictionary where student data lives

|___ README.md

```

## How It Works

- Every student is stored as an entry in a dictionary, where the name's the key and the list of marks is the value.

- The `grading.py` file converts a list of marks into an average. Then turns that average into a letter grade according to this scale:

| Average Marks | Grade |

|---|---|

| 90 and above | A+ |

| 80 – 89 | A |

70 – 79 | B |

| 60 – 69 | C |

| 50 – 59 D |

| Below 50 | F |

## Setup Instructions

1. Ensure that Python 3 is installed on your computer.

2.. Clone this repository:

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

When you run the program you will see a menu like this:

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

Simply type the number corresponding to what you want to do and follow the prompts. For example selecting **1** will ask for a students name. Then for marks in each subject before saving the record.

## Future Improvements

- Save student records, to a file or database ensuring that student records do not disappear when the program exits.

- Add input validation preventing the program from crashing when bad input is entered.

- Add a feature that allows editing the mark for one subject avoiding the need to re-enter all subject marks.

- Write tests to confirm that the grading logic works correctly.

## Author

Siddharth Mahapatra
