a01 = open('Input/students.txt', 'r')
a02 = a01.read()

lengths = [str(len(name)) for name in a02.split()]


a03 = open ('Output/output15.txt', 'w')
a04 = a03.write('\n'.join(lengths))