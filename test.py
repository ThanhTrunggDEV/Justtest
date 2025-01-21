class Employee:
    age = 18
    def __init__(self,name, employee_id, department, salary):
        self.name = name
        self.employee_id = employee_id
        self.department = department
        self.salary = salary
    def get_details(self):
        return (f"ID: {self.employee_id}\n"
                f"Name: {self.name}\n"
                f"Department: {self.department}\n"
                f"Salary: {self.salary}")
    def update_salary(self, new_salary):
        self.salary = new_salary
    def sayhi():
        print("Hi")

def main():
    employ = Employee("Ryan", "NV12", "IT", 10000000000000)
    Employee.age = 25
    print(employ.age)
    employ.age = 20
    print(employ.age)
    print(Employee.age)

main()