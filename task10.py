a01 = open('Input/numbers.txt', 'r')
a02 = a01.read()

numbers = [int(num) for num in a02.split()]
numbers.sort()

a03 = open ('Output/output10.txt', 'w')
a04 = a03.write(str(numbers))