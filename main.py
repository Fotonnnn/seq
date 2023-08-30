class Employee:
    def __init__(self, emp_id, name, position, salary):
        self.emp_id = emp_id
        self.name = name
        self.position = position
        self.salary = salary

class EmployeeManagementSystem:
    def __init__(self):
        self.employees = {}

    def add_employee(self, emp_id, name, position, salary):
        if emp_id not in self.employees:
            self.employees[emp_id] = Employee(emp_id, name, position, salary)
            print(f"Employee {name} added successfully.")
        else:
            print(f"Employee with ID {emp_id} already exists.")

    def view_employee(self, emp_id):
        if emp_id in self.employees:
            employee = self.employees[emp_id]
            print(f"Employee ID: {employee.emp_id}")
            print(f"Name: {employee.name}")
            print(f"Position: {employee.position}")
            print(f"Salary: ${employee.salary}")
        else:
            print(f"Employee with ID {emp_id} not found.")

    def update_employee(self, emp_id, name=None, position=None, salary=None):
        if emp_id in self.employees:
            employee = self.employees[emp_id]
            if name:
                employee.name = name
            if position:
                employee.position = position
            if salary:
                employee.salary = salary
            print(f"Employee {employee.name} updated successfully.")
        else:
            print(f"Employee with ID {emp_id} not found.")

    def delete_employee(self, emp_id):
        if emp_id in self.employees:
            employee = self.employees.pop(emp_id)
            print(f"Employee {employee.name} deleted successfully.")
        else:
            print(f"Employee with ID {emp_id} not found.")

if __name__ == "__main__":
    emp_system = EmployeeManagementSystem()

    while True:
        print("\nEmployee Management System")
        print("1. Add Employee")
        print("2. View Employee")
        print("3. Update Employee")
        print("4. Delete Employee")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            emp_id = input("Enter employee ID: ")
            name = input("Enter employee name: ")
            position = input("Enter employee position: ")
            salary = float(input("Enter employee salary: "))
            emp_system.add_employee(emp_id, name, position, salary)
        elif choice == "2":
            emp_id = input("Enter employee ID: ")
            emp_system.view_employee(emp_id)
        elif choice == "3":
            emp_id = input("Enter employee ID: ")
            name = input("Enter updated name (leave empty to skip): ")
            position = input("Enter updated position (leave empty to skip): ")
            salary = input("Enter updated salary (leave empty to skip): ")
            if salary:
                salary = float(salary)
            emp_system.update_employee(emp_id, name, position, salary)
        elif choice == "4":
            emp_id = input("Enter employee ID: ")
            emp_system.delete_employee(emp_id)
        elif choice == "5":
            print("Exiting the Employee Management System.")
            break
        else:
            print("Invalid choice. Please select a valid option.")
