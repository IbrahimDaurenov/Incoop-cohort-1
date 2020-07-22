

def quadratic(x): #function with 1 argument
    a = x*x + 4*x + 4
    return a


print(quadratic(1))
print(quadratic(2))
print(quadratic(3))
print(quadratic(4))
print(quadratic(5))
print(quadratic(0))


def friends(a,b,c): #function with 3 arguments
    return [a,b,c]

print(friends('John', 'Alex', 'Bob'))


def multiple_friends(*args):
    my_list = []

    for e in args:
        my_list.append(e)

    return my_list

print(multiple_friends('A','B','C','D','E'))
print(multiple_friends('A','B','C'))
print(multiple_friends('A','B','C','D','E','F'))
print(multiple_friends('A','B','C','D','E', 1, 2, 3, 4, 5))


def greetings(name): #function which does not return anything
    print('Hello, '+ name)

greetings('Daniyar')


def hello():
    print('Hello world!')
hello()
