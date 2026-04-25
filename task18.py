a01 = open('Input/students.txt', 'r')
a02 = a01.read()

user_name = input("Ism kiriting: ")

if user_name in a02.split():
    result = "FOUND"
else:
    result = "NOT FOUND"


a03 = open ('Output/output18.txt', 'w')
a04 = a03.write(result)