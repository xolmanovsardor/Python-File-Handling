a01 = open('Input/numbers.txt', 'r')
a02 = a01.read()

result = 0

for num in a02.split():
    result += int(num)

a03 = open ('Output/output02.txt', 'w')
a04 = a03.write(str(result))