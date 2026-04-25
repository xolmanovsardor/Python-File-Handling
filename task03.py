a01 = open('Input/numbers.txt', 'r')
a02 = a01.read()

result = max(int(num) for num in a02.split())

a03 = open ('Output/output03.txt', 'w')
a04 = a03.write(str(result))