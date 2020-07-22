# How many natural square numbers less than 1,000,000 are also multiples of 24?

my_list = []

for i in range(1000):
    sq = i*i
    if (sq%24==0):
        my_list.append(sq)

print(len(my_list))
print(my_list)


print(len([ i*i for i in range(1000) if i*i%24==0]))

print(my_list)
