"""Tests for the student grade tracker."""

import unittest

from test import Student


class StudentTests(unittest.TestCase):
    """Verify student identity, grade validation, and reports."""

    def setUp(self):
        """Create a student for each test."""
        self.student = Student("S-1", "Ada Lovelace")

    def test_identity_fields_must_not_be_empty(self):
        """Reject blank names and IDs."""
        with self.assertRaisesRegex(ValueError, "Student ID cannot be empty"):
            Student("  ", "Ada")
        with self.assertRaisesRegex(ValueError, "Student name cannot be empty"):
            Student("S-1", "  ")

    def test_add_grade_rejects_non_numeric_and_out_of_range_values(self):
        """Reject grades that are not numeric or outside 0-100."""
        self.assertFalse(self.student.add_grade("Fifty"))
        self.assertFalse(self.student.add_grade(True))
        self.assertFalse(self.student.add_grade(-1))
        self.assertFalse(self.student.add_grade(101))
        self.assertEqual(self.student.grades, [])

    def test_average_letter_and_status_thresholds(self):
        """Calculate averages and apply the required grade boundaries."""
        expected_letters = (
            (100, "A"),
            (90, "A"),
            (89, "B"),
            (80, "B"),
            (79, "C"),
            (70, "C"),
            (69, "D"),
            (60, "D"),
            (59, "F"),
            (0, "F"),
        )
        for grade, expected_letter in expected_letters:
            with self.subTest(grade=grade):
                student = Student("S-2", "Grace Hopper")
                self.assertTrue(student.add_grade(grade))
                self.assertEqual(student.calc_average(), grade)
                self.assertEqual(student.letter_grade, expected_letter)
                self.assertEqual(student.is_passed, grade >= 60)
                self.assertEqual(student.honor, grade >= 90)

    def test_empty_student_has_zero_average_and_fails(self):
        """Return safe defaults before any grades have been added."""
        self.assertEqual(self.student.calc_average(), 0.0)
        self.assertEqual(self.student.letter_grade, "F")
        self.assertFalse(self.student.is_passed)
        self.assertFalse(self.student.honor)

    def test_delete_grade_by_value(self):
        """Delete one matching grade and handle missing values."""
        self.student.add_grade(75)
        self.student.add_grade(75)
        self.assertTrue(self.student.delete_grade_by_value(75))
        self.assertEqual(self.student.grades, [75])
        self.assertFalse(self.student.delete_grade_by_value(90))

    def test_delete_grade_by_index(self):
        """Delete by valid index and handle invalid indexes."""
        self.student.add_grade(70)
        self.student.add_grade(80)
        self.assertTrue(self.student.delete_grade(0))
        self.assertEqual(self.student.grades, [80])
        self.assertFalse(self.student.delete_grade(4))
        self.assertFalse(self.student.delete_grade("0"))

    def test_report_contains_required_summary_fields(self):
        """Include identity, count, average, letter, status, and honor state."""
        self.student.add_grade(90)
        summary = self.student.report()
        for field in (
            "ID: S-1",
            "Name: Ada Lovelace",
            "Grades count: 1",
            "Average: 90.00",
            "Letter grade: A",
            "Status: Passed",
            "Honor roll: True",
        ):
            with self.subTest(field=field):
                self.assertIn(field, summary)


if __name__ == "__main__":
    unittest.main()
