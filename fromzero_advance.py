# def student_result():

#     name = input("Enter student name: ")

#     total = 0

#     for i in range(1,4):
#         marks = int(input(f"Enter marks subject {i}: "))
#         total = total + marks

#     average = total / 3

#     if average >= 80:
#         grade = "A"

#     elif average >= 60:
#         grade = "B"

#     elif average >= 40:
#         grade = "C"

#     else:
#         grade = "Fail"

#     print("\nStudent Name:",name)
#     print("Total Marks:",total)
#     print("Average:",average)
#     print("Grade:",grade)


# student_result()









def student_result():
    name=input("enter your name :")
    total=int(input("enter the toatal: "))
    obt=0
    for subject in range(1,4):
        marks=float(input(f"enter your marks {subject} :"))
        obt +=  marks
    percentage= (obt/total)*100
    print("Name:",name)
    print("Obtained Marks:",obt)
    print("you get %=", percentage)
    if percentage >= 80:
        print("A ")
    elif percentage >=60:
        print("B")
    elif percentage >= 50:
        print("C")
    else:
        print("F")
            
student_result() 



# def student_result():
#     name=input("Enter your name : ")

#     total=300
#     obt=0

#     for subject in range(1,4):
#         marks=int(input(f"Enter marks of subject {subject}: "))
#         obt += marks

#     percentage=(obt/total)*100

#     print("Name:",name)
#     print("Obtained Marks:",obt)
#     print("Percentage:",percentage)

#     if percentage >=80:
#         print("Grade: A")

#     elif percentage >=60:
#         print("Grade: B")

#     elif percentage >=50:
#         print("Grade: C")

#     else:
#         print("Grade: F")

# student_result()