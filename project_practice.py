while True:
    print("="*20 + "login panel" + "="*20)
    user=input("enter your username :")
    password=input("enter your password :") 


    if user == "qamar" and password =="12345":
     

     print("\nlogin successfully")
     break
    else:
       print("iNvalide login")
    print("="*20 + "..." + "="*20)


import os
while True:
    print("="*20 + "..." + "="*20)
    print("press 1: view data")
    print("press 2: add data")
    print("press 3: remove data")
    print("press 4: update data")
    print("press 0: Exit system")

    choice=int(input("choice :"))
    match choice:
        case 0:
            print("\nExit system")
         
        case 1:
            print("="*10 +"view employee records" +"="*10)
            try:
                with open("worker.txt","r")as file:
                    data_a= file.readlines()
                    count=0

                for worker in data_a:
                    count+=1
                    data=worker.strip().split("||")
                    print("="*10 +"view employee records" +"="*10)
                    print("worker|_id",data[0])
                    print("worker|_name",data[1])
                    print("worker|_email",data[2])
                    print("department",data[3])
                    print("salary",data[4])
                    if  count==0:
                        print("file is empty")
                        
            except FileNotFoundError:
             
        
   
        
             with open("worker.txt","x"):
               print("file is created")
               input("to be continue.....")
        case 2:
    
            print("="*10 +"add employee records" +"="*10)
            with open("worker.txt","a")as file:
                worker_id=input("enter your id :").strip()
                worker_name=input("enter your name :").strip()
                worker_email=input("enter your email :").strip()
                department=input("enter your department").strip()
                salary=input("enter your salary").strip()   

                file.write(f"{worker_id}||{worker_name}||{worker_email}||{department}||{salary}\n")
                print("\nsuccessfully added data")

            input("to be continue...") 
    

                  





            
                
                
