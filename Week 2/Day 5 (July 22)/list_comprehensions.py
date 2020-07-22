




my_list = [123,1,1,2,31,31,213,123,123,12312]

#new_list = []

#for e in my_list:
#    if (e%2==1):
#        new_list.append(e)

new_list = [ e for e in my_list if e%2==0]
print(new_list)




# a = [ F(e) for e in ITERABLE if CONDITION]
