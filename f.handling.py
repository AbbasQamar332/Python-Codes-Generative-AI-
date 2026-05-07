# with open("student1.txt","w")as file:
#     for num in range(5):
#         name=input("enter your names :")
#         file.write(name +"\n")
# print("write name successfully")


# count=0
# with open("student1.txt","r")as file:
#     for line in file:
#         print(line.strip())
#         count+=1
#     print("Total name :",count)         



with open("student1.txt","a")as file:
    for i in range(2):
        name=input("enter extra name :")
        file.write(name+"\n")
print("added name successfully")        