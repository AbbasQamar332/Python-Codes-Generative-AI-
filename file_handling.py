 
# with open("students.txt", "w") as file:    
#     for i in range(5):
#         name = input("Enter student  name: ")
#         file.write(name + "\n")
# print("Data written successfully!")

count = 0

# with open("students.txt", "r") as file:
#     for line in file:
#         print(line.strip()) 
#         count += 1

# print("Total names:", count)


# with open("students.txt", "a") as file:
#     for i in range(2):
#         name = input(f"Enter extra student {i+1}: ")
#         file.write(name + "\n")

# print("Names added successfully")


# numbers = []

# for i in range(5):
#     num = int(input(f"Enter number {i+1}: "))
#     numbers.append(num)
# with open("numbers.txt", "w") as file:
#     file.write("\n".join(map(str, numbers)))
# with open("numbers.txt", "r") as file:
#     data = file.read()
# nums = list(map(int, data.split(",")))
# total = sum(nums)
# avg = total / len(nums)
# print("Sum:", total)
# print("Average:", avg )

# with open("students.txt", "r") as file:
#     data = file.read()
# with open("students_backup.txt", "w") as file:
#     file.write(data)
# print("Backup created successfully!")
# with open("story.txt", "w") as file:
#     file.write("This is a simple story.\nIt has multiple lines.\nPython is easy.")
# with open("story.txt", "r") as file:
#     data = file.read()
# words = len(data.split())
# characters = len(data)
# lines = len(data.splitlines())
# # print("Words:", words)
# # print("Characters:", characters)
# print("Lines:", lines)






# task1

# with open("student2.txt","w") as file:
#     for i in range(5):
#         num= input("enter your name :")
#         file.write(num +"\n")
#     print("writen data successfully")

# task2
# count=0
# with open("students.txt","r") as file:
#     for line in file:
#         print(line.strip())
#         count+=1
# print("total names:",count)        



# task3
# with open ("students.txt","a") as file:
#     for i in range(2):
#         name=input("enter your name :")
#         file.write(name +"\n")
# print("add name successfully")

# task 4
with open("numbers.txt","w")as file:
    number=[]
    for i in range(5):
     num=input("enter your number :")
     number.append(num)
     file.write("," .join(number))
    
    print("="*20)
with open("numbers.txt","r")as file:
   number=file.read().split(",") 
   sum=0
   for num in number:
      print(num)
      sum+=int(num)
print("sum of number :",sum)
print("average of number:",sum/len(number))      
   
