class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_details(self):
        return f"Employee: {self.name}, Salary: {self.salary}"

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def get_details(self):
        return f"Manager: {self.name}, Salary: {self.salary}, Department: {self.department}"

# Introducerea datelor de la tastatură
name_emp = input("Enter the employee's name: ")
salary_emp = float(input("Enter the employee's salary: "))

# Crearea obiectului Employee
emp = Employee(name_emp, salary_emp)

name_mgr = input("Enter the manager's name: ")
salary_mgr = float(input("Enter the manager's salary: "))
department_mgr = input("Enter the manager's department: ")

# Crearea obiectului Manager
mgr = Manager(name_mgr, salary_mgr, department_mgr)

# Afisarea detaliilor
print(emp.get_details())  # "Employee: John, Salary: 3000"
print(mgr.get_details())  # "Manager: Alice, Salary: 5000, Department: IT"
