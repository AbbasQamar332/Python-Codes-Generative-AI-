# import datetime
# class myclass:
#     def __init__(self, classname, student_count, campus):
#         self.name = classname
#         self.campus = campus
#         self.student =student_count

#         pass
# c1=myclass("ali",26,"AKT")
# print(c1)
    
            

import datetime

class MyClass:

    def __init__(self, classname, student_count, campus):
        self.name = classname
        self.student = student_count
        self.campus = campus
        self.city="Lahore"
        self.creat_at= datetime.datetime.now()
    def __str__(self):
        return f"Name: {self.name}\nStudents: {self.student}\nCampus: {self.campus} \n{self.creat_at}\n{self.city}"


c1 = MyClass("Ali", 26, "AKT")

print(c1)