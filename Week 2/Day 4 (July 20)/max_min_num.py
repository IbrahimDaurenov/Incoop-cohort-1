my_list = []

num = int(input('Number: '))

while(num!=-999999):
    my_list.append(num)
    num = int(input('Number: '))


maximum = my_list[0]

for e in my_list:
    if e > maximum:
        maximum = e

print(maximum)



#print(max(my_list))
#print(min(my_list))
