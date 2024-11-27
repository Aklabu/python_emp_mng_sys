import os

class EmployeeManager:
    def __init__(self, filename="employees.txt"):
        self.filename = filename
        self.employees = self.load_employees()

    def load_employees(self):
        if not os.path.exists(self.filename):
            return []
        with open(self.filename, "r") as file:
            lines = file.readlines()
            employees = [self.parse_employee(line) for line in lines]
        return employees

    def save_employees(self):
        with open(self.filename, "w") as file:
            for emp in self.employees:
                file.write(f"{emp.emp_id},{emp.name},{emp.designation}\n")

    def parse_employee(self, line):
        emp_id, name, designation = line.strip().split(",")
        return Employee(emp_id, name, designation)

    def add_employee(self, employee):
        self.employees.append(employee)
        self.save_employees()

    def update_employee(self, emp_id, name=None, designation=None):
        for emp in self.employees:
            if emp.emp_id == emp_id:
                if name:
                    emp.name = name
                if designation:
                    emp.designation = designation
                self.save_employees()
                return True
        return False

    def delete_employee(self, emp_id):
        self.employees = [emp for emp in self.employees if emp.emp_id != emp_id]
        self.save_employees()

    def view_employees(self):
        return self.employees

    def search_employee(self, term):
        return [emp for emp in self.employees if term in emp.name or term in emp.designation]
