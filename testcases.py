import unittest
from test import Employee, Department
class TestEmployee(unittest.TestCase):
    def test_employee_creation(self):
        employee = Employee("Alice", "E001", "HR", 50000)
        self.assertEqual(employee.name, "Alice")
        self.assertEqual(employee.employee_id, "E001")
        self.assertEqual(employee.department, "HR")
        self.assertEqual(employee.salary, 50000)

    def test_update_salary(self):
        employee = Employee("Bob", "E002", "Engineering", 75000)
        employee.update_salary(80000)
        self.assertEqual(employee.salary, 80000)

class TestDepartment(unittest.TestCase):
    def test_add_employee(self):
        department = Department("HR")
        employee = Employee("Charlie", "E003", "HR", 60000)
        department.add_employee(employee)
        self.assertIn(employee, department.employees)

    def test_remove_employee(self):
        department = Department("Engineering")
        employee = Employee("David", "E004", "Engineering", 70000)
        department.add_employee(employee)
        result = department.remove_employee("E004")
        self.assertEqual(result, 1)
        self.assertNotIn(employee, department.employees)

    def test_get_department_details(self):
        department = Department("HR", )
        employee1 = Employee("Eve", "E005", "HR", 45000)
        employee2 = Employee("Frank", "E006", "HR", 55000)
        department.add_employee(employee1)
        department.add_employee(employee2)
        details = department.get_department_details()
        self.assertTrue("Name: Eve" in details and "E005" in details)
        self.assertTrue("Name: Frank" in details)

