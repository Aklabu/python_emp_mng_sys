from employee import Employee
from employee_manager import EmployeeManager

def main():
    manager = EmployeeManager()

    while True:
        print("\nEmployee Management System")
        print("1. Add Employee")
        print("2. Update Employee")
        print("3. Delete Employee")
        print("4. View All Employees")
        print("5. Search Employee")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            emp_id = input("Enter Employee ID: ")
            name = input("Enter Employee Name: ")
            designation = input("Enter Employee Designation: ")
            emp = Employee(emp_id, name, designation)
            manager.add_employee(emp)
            print("Employee added successfully.")
        elif choice == "2":
            emp_id = input("Enter Employee ID to update: ")
            name = input("Enter new name (leave blank to skip): ")
            designation = input("Enter new designation (leave blank to skip): ")
            if manager.update_employee(emp_id, name, designation):
                print("Employee updated successfully.")
            else:
                print("Employee not found.")
        elif choice == "3":
            emp_id = input("Enter Employee ID to delete: ")
            manager.delete_employee(emp_id)
            print("Employee deleted successfully.")
        elif choice == "4":
            employees = manager.view_employees()
            for emp in employees:
                print(emp)
        elif choice == "5":
            term = input("Enter name or designation to search: ")
            results = manager.search_employee(term)
            for emp in results:
                print(emp)
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
