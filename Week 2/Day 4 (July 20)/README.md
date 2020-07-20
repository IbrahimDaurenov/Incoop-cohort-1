<center>Day 1 Outline</center>

<b>Git:</b>
<ul>
  <li> github.com/</li>
  <li> git init</li>
  <li> git add -A</li>
  <li> git commit -m "Initial commit"</li>
  <li> git remote add origin remote repository URL </li>
  <li> git remote -v </li>
  <li> git push -u origin master </li>
</ul>

<b>Python 1: </b>
<ul>

  <li> variables </li>
  <li> input/output </li>
  <li>
    Ints

```
      a = 10
      x = 123
      y = a + 1 #->this results in y = 11
      a = a * 2 #->this results in y = 20
      z = 9**2  #->this results in y = 81
      a = x//2  #->this results in a = 61


```
  </li>
  <li> Floats

```
        a = 10.5
        x = math.pi
        y = 122.0
        z = x/y
        t = a/1
```
  </li>
  <li>
  Strings

  ```
        a = 'Hello world'
        b = 'Daniyar'
        c = a + b # ->this results in c = 'Hello worldDaniyar'
        len(a) # number of chars in a, which is 11
        a[0] # first char of a, which is H
        a[-1] # last char of a, which is D
        a[3:5] # part of a from 4th to 6th chars, which is 'o w'
  ```
  </li>
  <li> Lists

```
        my_list = [1,2,3]
        my_list2 = [1,'Hello', 5.5]
        my_list3 = [1,2,3, ['lol', 1, 2], 'Hello world']
        my_list[0] # first element of the list
        len(my_list) # number of elements in the list
        new_list = my_list.copy() copying list
        new_list.pop
```

  </li>
  <li> Tuples </li>
  <li> Sets</li>
  <li> Dictionaries </li>
  <li> Conditionals </li>
  <li> Loops</li>
  </ul>




<b>Homework 3:</b>

Ex. 1: You need to write a program, that will ask a user to type a name of some country. If this country is in top-25 (by the size) then you should print 'Asia' or 'America' or 'Africa', you should print the link to wikipedias link. You are not allowed to use ANY libraries (exception: webbrowser if you want extra-credit). Try to use data-types covered in Day 4.

Ex 2. Write a python program that validates the password. First of all, ask for a password. Then check if:

 - It has at least one lower case letter
 - It has at least one upper case letter
 - It has at least one digit
 - It has at least one special character
 - It has at least 10 characters
 - It has at most 15 characters

If password passes validity test then say 'Success' to user. Otherwise, ask to retype password until they type valid password.

Ex 3.
Write a program that will print letter "A" in a fancy way. Ask user for a size (integer number from 0 to 30) and type fancy A with the given size based on examples. Below you can find examples of how it must be printed:

If size = 1:
 *
***
* *

If size = 2:
 **
*  *
****
*  *
*  *

If size = 3:
 ***                                                                   
*   *                                                                  
*   *                                                                  
*****                                                                  
*   *                                                                  
*   *                                                                  
*   *



Ex 4.
Create Github repo and call it "Web Development Practice"
Upload HW1, HW2 and HW3 (in separate folders).
