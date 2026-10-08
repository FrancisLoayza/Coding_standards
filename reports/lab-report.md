# Coding Standards Lab Report

## Introduction

This project uses Pylint to check Python code because it reports errors, warnings, and style problems without requiring changes to the program's behavior. The public repository is available at <https://github.com/FrancisLoayza/Coding_standards>.

## Development

The initial report was generated with Pylint 4.1.2 against the original `test.py` retrieved from the repository's starting commit. It found 19 problems and returned exit code 22. The final report checks `test.py` and `test_student.py`; it found zero problems and Pylint rated the code 10.00/10.

The student grade tracker now validates non-empty names and IDs, accepts numeric grades from 0 through 100, calculates averages and letter grades, determines Passed/Failed and honor-roll status, deletes grades by value or index, and prints the required summary. Invalid input prints a clear error and returns to the menu instead of terminating the program. Seven unit tests cover the main rules and error cases.

The GitHub Actions workflow is stored at `.github/workflows/lint.yml`. It is configured for pull requests targeting `main` and can also be started manually. Its current actor filter means the lint job runs only when the GitHub actor is `FrancisLoayza`; if the rubric requires linting every contributor's pull request, remove that filter.

### Initial report

![Initial Pylint report showing 19 problems](pylint-initial.png)

[Open the initial HTML report](pylint-initial.html)

### Final report

![Final Pylint report showing zero problems](pylint-final.png)

[Open the final HTML report](pylint-final.html)

## Conclusions

The final code meets the listed grade-tracking requirements, passes all seven unit tests, and has no Pylint findings. The initial and final reports document the improvement from the original code.

## Recommendations

- Push the finished code and reports to the public repository and confirm the workflow succeeds in the GitHub Actions tab.
- Keep the actor filter only if the assignment explicitly requires restricting execution to this account; otherwise remove it so every pull request to `main` is linted.
- Include screenshots of the successful test run and GitHub Actions run if the instructor expects evidence beyond the two Pylint report captures.