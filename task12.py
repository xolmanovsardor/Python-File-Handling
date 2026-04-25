a01 = open('Input/students.txt', 'r')
a02 = a01.read()

c = str(len(a02.split()))


a03 = open ('Output/output12.txt', 'w')
a04 = a03.write(c)