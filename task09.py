a01 = open('Input/numbers.txt', 'r')
a02 = a01.read()

c = ' '.join(str(len(num)) for num in a02.split())

a03 = open ('Output/output09.txt', 'w')
a04 = a03.write(c)