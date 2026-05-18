while True:
      print("="*20 +"admin login"+"="*20 +"\n")
      username=input("enter username :").strip()
      pasword=input("enter your password :").strip()


      if username=="qamar" and pasword=="123456" :
      
        print("\nlogin sucessfully")
        break
      
      else:
          print("login fail incorrect username and password")
        
  
import os
while True:
    print("="*20 +"admin panel"+"="*20 +"\n") 
    print("press 1 :view data ")
    print("press 2 :add data")
    print("press 3  :remove data :")
    print("press 4  : update data :")
    print(" press 0 :exit data :")  

    choice=int(input("enter choice :"))  

    match choice:
        case 0:
            print("\nsystem exit")
            break
        case 1:
            print("="*10 + "view employee data"+"="*10)
            try:
               with open("employee2.txt", "r")as file:
                 count=0


                 for employee2 in file:
                  

                  count+=1
                  data=employee2.strip().split("||")
                  print("=======",count,"=======")
                  print("employee id",data[0])
                  print("employee name",data[1])
                  print("employee email",data[2])
                  print("department",data[3])
                  print("salary",data[4])
                 count==0
                 print("\n")
                       
            except  FileNotFoundError:
                
             with open("employee2.txt","x")as file:
                print("employee2.txt created") 
            input("to be continue...")   
        case 2:
                print("="*10 + "add employee data"+"="*10)
                with open("employee2.txt","a")as file:
                    emp_id=input("enter employee id :")
                    emp_name=input("enter employee name :")
                    emp_email=input("enter employee email :")
                    department=input("enter department :")
                    salary=input("enter salary :")
                    file.write(f"{emp_id}||{emp_name}||{emp_email}||{department}||{salary}\n") 
                    print("enter added successfully")
                input("To be continue....")
        case 3:
            print("="*10 + " remove employee"+"="*10)
            emp_id=int(input("enter your id :"))
            found= False  
            with open("employee2.txt","r") as file:
                records =file.readlines()                     
                for employee in records:
                    record = employee.strip().split("||")
                    if int(record[0]) ==  emp_id:
                        found = True
                        records.remove(employee)
                        print("Remove record Successfully")
                        break

            if found:
                with open("employee2.txt","w") as file:
                    file.writelines(records)
                    print("account deleted")
                    input("remove successfully")
            else:
                print("there is no file found ")        
        case 4:
             print("="*10 + "update employee"+"="*10)
             update_id = input("enter employee id :").strip()
             found=False
             updated_data=[]
              
             with open("employee2.txt","r")as file:
                 records =file.readlines()

                 for employee in records:
                     record = employee.strip().split("||")
                     if record[0] == update_id:
                         found=True
                         print("\nenter new details")
                         new_name = input("enter your new name :").strip()
                         new_email = record[2]
                         new_department = input("enter your department :").strip()
                         new_salary = input("enter your salary :").strip()
                         
                         record[0] = update_id
                         record[1] = new_name
                         record[2] = new_email
                         record[3] = new_department
                         record[4] = new_salary 
                         updated_data = (f"{update_id}||{new_name}||{new_email}||{new_department}||{new_salary}\n")
                         break
                 if found:
                    with open("employee2.txt","w")as file:
                        file.writelines(updated_data)
                        print("\nupdate successfully")
                        input("To be continue....")
                 else:
                     print("\nInvalid choice")
    os. system("cls")                                     

                     
                                 

                 






                






            



                

                  

   

                


   