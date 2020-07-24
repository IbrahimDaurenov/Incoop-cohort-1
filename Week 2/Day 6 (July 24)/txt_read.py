



file = open('othello.txt' , 'r')

#print (file.read()) # reads the whole file

#print (file.readline()) # reads a single line of the file
#print (file.readline(3)) # First three characters of the file
#print (file.readlines()) # Separates all lines of the file and puts them into a list
counter = 1

for line in file:
    #iterating throght the file
    print('Line N' + str(counter) + ': ' + line)
    counter += 1
file.close()
