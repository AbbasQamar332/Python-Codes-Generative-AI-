while True:
    print("="*20,"Login Page","="*20)
    username = input("Enter Username : ")
    password = input("Enter Password : ")
    if username == "admin" and password == "12345":
        print("Login Successfully!")
        break
    else:
        print("Invalid username or password")


import os
while True:
    print("=="*20,"Admin Panel","=="*20)
    print("=*= Press 1 to view record =*=")
    print("=*= Press 2 to add record =*=")
    print("=*= Press 3 to remove record =*=")
    print("=*= Press 4 to update record =*=")
    print("=*= Press 0 to exit =*=")

    choice = int(input("Choice : "))
    match choice:
        case 0:
            print("The program is ended")
            break
        case 1:
            try:
                count= 0
                with open("Records.txt","r") as file:
                    for data in file:
                        count +=1
                        print("="*20,count,"="*20)
                        data = data.strip().split("||")
                        print("Name   :       ",data[0])
                        print("Email  :      ",data[1])
                        print("Age    :      ",data[2])

            except FileNotFoundError:
                with open("Records.txt","w") as file:
                    file.write()
                    print("Create file successfully!")
            except Exception as e:
                print(e)
            input("\nPress Enter to continue...")
        case 2:
            print("Add Record")
            name = input("Enter Name : ").strip()
            email = input("Enter Email : ").strip()
            age = input("Enter Age : ").strip()
            data = f"{name} || {email} || {age}\n"
            with open("Records.txt","a") as file:
                file.write(data)
                print("Record added successfully!")
            input("\nPress Enter to continue...")
        case 3:
            print("Remove Record")
            email = input("email : ")
            is_found = False
            new_list = []
            with open("Records.txt","r")as file:
                data = file.readlines()
                for student in list(data):
                        record = student.strip().split("||")
                        new_list.append(record)
                        if  record[1].strip() == email:
                                is_found = True
                                data.remove(student)
                                break 
                        if is_found:
                            with open("Records.txt","w") as file:
                                file.writelines(data)
                                print("Record removed successfully!")
                        else:
                                    print("Record not found!")
                                
            
        case 4:
            print("Update Record")
            input("\nPress Enter to continue...")
        case _:
            print("invalid Entry")
    os.system("cls")