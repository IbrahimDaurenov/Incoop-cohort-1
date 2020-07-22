def function():
    year = input('Year: ')

    try:
        year = int(year)
    except:
        print('!!!!!Invalid input!!!!')
        function()

    age = (2020 - year)

    print(age)


function()
