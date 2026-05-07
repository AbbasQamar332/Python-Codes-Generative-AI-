# try:
#     y = 6/input("Enter a number: ")
# except TypeError:
#     print("Invalid Datatype")
# except ZeroDivisionError:
#     print("Zero cannot divide any number")
# except ValueError:
#     print("Invalid value")
# else:
#     print("No Error")
# finally:
#     print("Try body run successfully")


try:
    with open("students.txt","r") as file:
        print(file.read())
except FileExistsError:
    print("File is not found")
except PermissionError:
    print("this file is not allowed for Zeeshan")
except Exception as e:
    print(e)
else:
    print("No error")
finally:
    print("Run try body successfully")