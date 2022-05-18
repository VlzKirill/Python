filename= 'programming.txt'

with open (filename, 'w') as file_object:
    file_object.write("I love programming. \n")

with open (filename, 'a') as file_object:
    file_object.write('Append one more string. \n')
