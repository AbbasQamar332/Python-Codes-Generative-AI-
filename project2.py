



while True:
    print("=" * 20 + " LOGIN PANEL " + "=" * 20)

    username = input("Enter Username : ").strip()
    password = input("Enter Password : ").strip()

    if username == "abbas" and password == "123456":
        print("\nSuccessfully Login")
        break
    else:
        print("\nInvalid Username or Password")

import os
while True:

    print("\n" + "=" * 20 + "admin panel"   + "=" * 20)

    print("Press 1 : check balance")
    print("Press 2 : deposite")
    print("Press 3 : withdraw")
    print("Press 0 : Exit")

    choice = int(input("\nEnter Choice : "))

   

    match choice:
        case 0:
            print("\nSystem Closed")
            break
        
        case 1: 
    
            print("\n========== check balance ==========")
            
            try:
                with open(filename, "r") as file:

                    count = 0

                    for employee in file:

                        count += 1

                        data = employee.strip().split("||")

                        print("\n" + "=" * 10, count, "=" * 10)
                        print("check balance   :", data[0])
                        print("deposit :", data[1])
                        print("withdraw :", data[2])
                        

                    if count == 0:
                        print("No Employee Record Found")

            except FileNotFoundError:
                    with open(filename, "x"):
                        print("Employee File Created")

            input("\nPress Enter To Continue...")

   

        case 2:

            print("\n========== ADD EMPLOYEE ==========")

            with open(filename, "a") as file:

                emp_id = input("Enter Employee ID : ").strip()
                emp_email = input("Enter Employee Email : ").strip()
                emp_name = input("Enter Employee Name : ").strip()
                department = input("Enter Department : ").strip()
                salary = input("Enter Salary : ").strip()

                file.write(f"{emp_id}||{emp_email}||{emp_name}||{department}||{salary}\n")

                print("\nEmployee Added Successfully")

            input("\nPress Enter To Continue...")

   

        case 3:

            print("\n========== REMOVE EMPLOYEE ==========")

            remove_id = input("Enter Employee ID : ").strip()

            found = False
            new_data = []

            try:
                with open(filename, "r") as file:

                    records = file.readlines()

                    for employee in records:

                        data = employee.strip().split("||")

                        if data[0] == remove_id:
                            found = True
                        else:
                            new_data.append(employee)

                    with open(filename, "w") as file:
                        file.writelines(file)

                    if found:
                        print("\nEmployee Removed Successfully")
                    else:
                        print("\nEmployee ID Not Found")
            except FileNotFoundError:
                print("\nFile Not Found")

            input("\nPress Enter To Continue...")

    

        case 4:

            print("\n========== UPDATE EMPLOYEE ==========")

            update_id = input("Enter Employee ID : ").strip()
            found = False
            updated_data = []

            try:
                with open(filename, "r") as file:

                    records = file.readlines()

                    for employee in records:

                        data = employee.strip().split("||")

                        if data[0] == update_id:

                            found = True

                            print("\nEnter New Details")

                            new_name = input("Enter New Name : ").strip()
                            new_department = input("Enter New Department : ").strip()
                            new_salary = input("Enter New Salary : ").strip()

                            updated_data.append(
                                f"{update_id}||{new_name}||{new_department}||{new_salary}\n"
                            )

                        else:
                            updated_data.append(employee)

                with open(filename, "w") as file:
                    file.writelines(updated_data)

                if found:
                    print("\nEmployee Updated Successfully")
                else:
                    print("\nEmployee ID Not Found")

            except FileNotFoundError:
                print("\nFile Not Found")

    input("\nPress Enter To Continue...")

   

else:
        print("\nInvalid Choice")


os.system("cls")

                            