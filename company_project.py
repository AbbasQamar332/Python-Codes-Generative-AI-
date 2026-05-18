class Employee:

    def __init__(self, employee_id, name, department, salary, present_days):
        self.employee_id = employee_id
        self.name = name
        self.department = department
        self.salary = salary
        self.present_days = present_days


    def calculate_bonus(self):

        if self.present_days >= 26:
            bonus = 5000

        elif self.present_days >= 22:
            bonus = 3000

        else:
            bonus = 1000

        return bonus


    def final_salary(self):

        total = self.salary + self.calculate_bonus()

        return total


    def show_info(self):

        print("\nEmployee ID:", self.employee_id)
        print("Name:", self.name)
        print("Department:", self.department)
        print("Salary:", self.salary)
        print("Present Days:", self.present_days)
        print("Bonus:", self.calculate_bonus())
        print("Final Salary:", self.final_salary())


def add_employee():

    employee_id = input("Enter Employee ID: ")
    name = input("Enter Name: ")
    department = input("Enter Department: ")

    salary = int(input("Enter Salary: "))
    present_days = int(input("Enter Present Days: "))

    emp = Employee(
        employee_id,
        name,
        department,
        salary,
        present_days
    )

    return emp


 


while True:

    print("\n===== MENU =====")
    print("1. Add Employee")
    print("2. View Employees")
    print("3. Exit")

    choice = input("Enter choice: ")


    if choice == "1":

        emp = add_employee()

        employees.append(emp)

        print("Employee Added Successfully")


    elif choice == "2":

        if len(employees) == 0:

            print("No Employee Found")

        else:

            for worker in employees:

                worker.show_info()


    elif choice == "3":

        print("Program Closed")

        break


    else:

        print("Invalid Choice")