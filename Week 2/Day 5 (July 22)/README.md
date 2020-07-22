<center>Day 1 Outline</center>


<b>Python 2: </b>
<ul>
  <li>

    Functions

```
  def foo(param):
    some action
    return value

  def main():
    main action

  if __name__ == '__main__':
    main()

```

  </li>
  <li> Modules

  ```
    import math

    math.PI
  ```


  ```
    import bar

    bar.foo()
  ```

  </li>
  <li> List comprehensions

  ```
    odds = [e for e in range(100) if e%2==1 ]

    [i for i in iterable if expression]

  ```

  </li>
  <li>
    Exceptions

    ```
      try:
        some action
      except:
        if action failed
    ```

  </li>

  <li>
    Date and Time

```
      from datetime import datetime, date, time
      d = date(2020, 7, 14)
      t = time(12, 30)
      datetime.combine(d, t)
      datetime.datetime(2005, 7, 14, 12, 30)
      # Using datetime.now() or datetime.utcnow()
      datetime.now()
      datetime.datetime(2007, 12, 6, 16, 29, 43, 79043)   # GMT +1
      datetime.utcnow()
      datetime.datetime(2007, 12, 6, 15, 29, 43, 79060)
      # Using datetime.strptime()
      dt = datetime.strptime("21/11/06 16:30", "%d/%m/%y %H:%M")
      dt
      datetime.datetime(2006, 11, 21, 16, 30)
      # Using datetime.timetuple() to get tuple of all attributes
      tt = dt.timetuple()
      for it in tt:
           print(it)
```
  </li>

  </ul>




<b>Homework:</b>
```
  Ex 1. Create your own cypher (call it cypher.py). You should ask your user to choose if he wants to encrypt or decrypt message. If he chooses to encrypt then ask for the message and then send him encrypted message. Otherwise, allow your to decrypt the message that he has got.

  Ex 2. Create a game (guess.py). Program should randomly generate a number between 1 and 10000 and user must guess this number. After each guess computer should respond with either: 'My number is greater', 'My number is less' or 'You guessed my number'.

  Ex 3. Create a program (time_machine.py) that asks user some date. After user typed the date your program should print either 'This date was N days ago' or 'This date will be in N days'. Make sure your program can understand all following inputs (without asking for some specific type): DD/MM/YYYY, DD.MM.YYYY, DD/MM/YY, DD.MM.YY, DD,MM,YY, DD.MM.YYYY

  Ex 4. Create a program hw4.py that will ask me to choose which exercise I want to grade. For example, if I choose Ex3, it should run time_machine.py.

```
