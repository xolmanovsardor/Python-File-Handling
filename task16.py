a01 = open('Input/students.txt', 'r')
a02 = a01.read()


filtered_names = [name for name in a02.split() if len(name) > 5]    

a03 = open ('Output/output16.txt', 'w')
a04 = a03.write('\n'.join(filtered_names))