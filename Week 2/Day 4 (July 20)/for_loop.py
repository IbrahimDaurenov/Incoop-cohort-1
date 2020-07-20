nums = [123,1232,4,4,68,83,1,24,43,75,634]
sum = 0

#iterate through a list
for e in nums:
    sum = sum + e

print(sum)

person = {
    'name': 'Daniyar',
    'age': 22,
    'height': 188.5,
    'students': ['Ibra', 'Yaroslav'],
}

for k,v in person.items():
    print(k,v)

sum = 0
for i in range( len(nums) ):
    sum += nums[i]

print(sum)



# for iterator:
#   action
