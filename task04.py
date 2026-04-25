a01 = open('Input/numbers.txt', 'r')
a02 = a01.read()

b01 = ' '.join(num for num in a02.split() if int(num) % 2 == 0)

a03 = open ('Output/output04.txt', 'w')
a04 = a03.write(b01)