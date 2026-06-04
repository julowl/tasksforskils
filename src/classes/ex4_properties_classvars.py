"""
Exercise 4 — Class variables and properties

Tasks:
- Implement Employee class that tracks the number of Employee instances via a class variable employee_count.
- Implement a full_name property (getter and setter) that combines first_name and last_name.
- Validate salary through a property (salary must be non-negative).

Run tests: python src/ex4_properties_classvars.py
"""
import unittest

class Employee:
    """Simple employee record.

    Class attributes:
        employee_count (int): number of Employee instances created
    """

    employee_count = 0

    def __init__(self, first_name: str, last_name: str, salary: float):
        """Initialize an Employee and increment employee_count.

        Raises:
            ValueError: if salary is negative or names are empty
        """
        raise NotImplemented

    @property
    def full_name(self) -> str:
        """Return 'First Last'."""
        raise NotImplemented

    @full_name.setter
    def full_name(self, value: str):
        """Set full_name splitting into first and last names.

        Raises:
            ValueError: if the value does not contain at least two parts
        """
        raise NotImplemented

    @property
    def salary(self) -> float:
        """Return the current salary."""
        raise NotImplemented

    @salary.setter
    def salary(self, value: float):
        """Set the salary, must be non-negative."""
        raise NotImplemented


# -------------------- Tests --------------------
class TestEmployee(unittest.TestCase):
    def setUp(self):
        # Reset count for testing isolation
        Employee.employee_count = 0

    def test_count_and_init(self):
        e1 = Employee('John', 'Doe', 3000)
        self.assertEqual(Employee.employee_count, 1)
        e2 = Employee('Jane', 'Roe', 4000)
        self.assertEqual(Employee.employee_count, 2)

    def test_full_name_property(self):
        e = Employee('Alice', 'Smith', 2000)
        self.assertEqual(e.full_name, 'Alice Smith')
        e.full_name = 'Alicia Smythe'
        self.assertEqual((e.first_name, e.last_name), ('Alicia', 'Smythe'))
        with self.assertRaises(ValueError):
            e.full_name = 'SingleName'

    def test_salary_validation(self):
        with self.assertRaises(ValueError):
            Employee('x', 'y', -1)
        e = Employee('x','y',1000)
        with self.assertRaises(ValueError):
            e.salary = -10


if __name__ == '__main__':
    unittest.main()
