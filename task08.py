a01 = open('Input/numbers.txt', 'r')
a02 = a01.read()


c = ' '.join(num for num in a02.split() if int(num) % 5 == 0)   



a03 = open ('Output/output08.txt', 'w')
a04 = a03.write(c)