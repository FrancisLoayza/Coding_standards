# Student Grade Tracker

Student grade tracker developed for a Python coding-standards lab. Pylint is used to check code quality, and the workflow runs it for pull requests targeting `main`.

## Features

- Create a student with a non-empty ID and name.
- Add numeric grades from 0 to 100.
- Calculate the average, letter grade, pass/fail status, and honor-roll status.
- Delete a grade by value or by zero-based index.
- Show a summary report. Invalid input displays an error and returns to the menu.

## Run

```bash
python3 test.py
```

Run the unit tests with:

```bash
python3 -m unittest test_student.py
```

## Reports

- [Lab report](reports/lab-report.md)
- [Initial Pylint report: 19 problems](reports/pylint-initial.html)
- [Final Pylint report: 0 problems](reports/pylint-final.html)

## GitHub Actions

The workflow is in `.github/workflows/lint.yml`. It is configured for pull requests targeting `main` and manual execution. The job currently runs only when the actor is `FrancisLoayza`.