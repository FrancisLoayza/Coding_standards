"""Simple student grade tracking example."""

MIN_GRADE = 0
MAX_GRADE = 100
PASSING_AVERAGE = 60
HONOR_AVERAGE = 90
LETTER_GRADE_THRESHOLDS = (
    (90, "A"),
    (80, "B"),
    (70, "C"),
    (60, "D"),
    (0, "F"),
)


class Student:
    """Store grades and report a student's results."""

    def __init__(self, student_id, name):
        """Create a student after validating the required identity fields."""
        if not isinstance(student_id, str) or not student_id.strip():
            raise ValueError("Student ID cannot be empty.")
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Student name cannot be empty.")
        self.student_id = student_id.strip()
        self.name = name.strip()
        self.grades = []

    @staticmethod
    def _is_number(value):
        """Return whether a value is a numeric grade, excluding booleans."""
        return isinstance(value, (int, float)) and not isinstance(value, bool)

    def add_grade(self, grade):
        """Add a grade if it is numeric and within the accepted range."""
        if not self._is_number(grade):
            print("Error: grade must be numeric.")
            return False
        if not MIN_GRADE <= grade <= MAX_GRADE:
            print(f"Error: grade must be between {MIN_GRADE} and {MAX_GRADE}.")
            return False
        self.grades.append(grade)
        return True

    def calc_average(self):
        """Return the average grade, or zero when there are no grades."""
        if not self.grades:
            return 0.0
        return sum(self.grades) / len(self.grades)

    @property
    def is_passed(self):
        """Return whether the student passed."""
        return self.calc_average() >= PASSING_AVERAGE

    @property
    def honor(self):
        """Return whether the student qualifies for the honor roll."""
        return self.calc_average() >= HONOR_AVERAGE

    def delete_grade(self, index):
        """Delete a grade by index, reporting invalid indexes without raising."""
        if isinstance(index, bool) or not isinstance(index, int):
            print("Error: grade index must be an integer.")
            return False
        if not 0 <= index < len(self.grades):
            print("Error: grade index is out of range.")
            return False
        del self.grades[index]
        return True

    def delete_grade_by_value(self, grade):
        """Delete the first matching grade, reporting missing values."""
        if not self._is_number(grade):
            print("Error: grade value must be numeric.")
            return False
        try:
            self.grades.remove(grade)
        except ValueError:
            print(f"Error: grade {grade} was not found.")
            return False
        return True

    @property
    def letter_grade(self):
        """Return the letter grade for the current average."""
        average = self.calc_average()
        for minimum, letter in LETTER_GRADE_THRESHOLDS:
            if average >= minimum:
                return letter
        return "F"

    def report(self):
        """Print a summary of the student's results."""
        summary = (
            f"ID: {self.student_id}\n"
            f"Name: {self.name}\n"
            f"Grades count: {len(self.grades)}\n"
            f"Average: {self.calc_average():.2f}\n"
            f"Letter grade: {self.letter_grade}\n"
            f"Status: {'Passed' if self.is_passed else 'Failed'}\n"
            f"Honor roll: {self.honor}"
        )
        print(summary)
        return summary


def main():
    """Run the interactive student grade tracker."""
    while True:
        try:
            name = input("Student name: ")
            student_id = input("Student ID: ")
            student = Student(student_id, name)
            break
        except ValueError as error:
            print(f"Error: {error}")

    while True:
        print("\n1. Add grade\n2. Delete grade by value\n"
              "3. Delete grade by index\n4. Show report\n5. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            try:
                grade = float(input("Grade (0-100): "))
            except ValueError:
                print("Error: enter a numeric grade.")
                continue
            student.add_grade(grade)
        elif choice == "2":
            try:
                grade = float(input("Grade to delete: "))
            except ValueError:
                print("Error: enter a numeric grade.")
                continue
            student.delete_grade_by_value(grade)
        elif choice == "3":
            try:
                index = int(input("Grade index to delete (starting at 0): "))
            except ValueError:
                print("Error: enter an integer index.")
                continue
            student.delete_grade(index)
        elif choice == "4":
            student.report()
        elif choice == "5":
            print("Goodbye.")
            return
        else:
            print("Error: choose an option from 1 to 5.")


if __name__ == "__main__":
    main()
