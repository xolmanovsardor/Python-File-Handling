a01 = open('Input/students.txt', 'r')
a02 = a01.read()


names = sorted(a02.split())

a03 = open ('Output/output13.txt', 'w')
a04 = a03.write('\n'.join(names))