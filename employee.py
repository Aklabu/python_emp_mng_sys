class Employee:
    def __init__(self, emp_id, name, designation):
        self.emp_id = emp_id
        self.name = name
        self.designation = designation
    
    def __str__(self):
        return f"ID: {self.emp_id}, Name: {self.name}, Designation: {self.designation}"
