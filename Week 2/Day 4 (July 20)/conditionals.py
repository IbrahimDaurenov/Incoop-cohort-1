num = int(input('Your number, please: '))

if (num > 0):
    print('Positive')
else:
    if (num==0):
        print('Zero')
    else:
        print('Negative')

if (num > 0):
    print('Positive')
elif (num==0):
    print('Zero')
else:
    print('Negative')


if (num%2==0 and num%3==0):
    print('Divisible by 2 and 3')
else:
    print('Not divisible by 2 and 3')


if (num>5 and num<10):
    print('Between 5 and 10')

if (10>num>5):
    print('Between 5 and 10')

if ( num<0 or num > 20):
    print('Invalid age')
else:
    print('Valid age')
