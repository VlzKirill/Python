filename = 'pi'
with open(filename) as file_object:
#    contents = file_object.read()
    lines = file_object.readlines()
#print(contents.rstrip())
#print(lines)
#pi_string = ''
#for line in lines:
#    print(line)
#    pi_string += line.strip()
#print(pi_string)
#print(len(pi_string))
#print (f'{pi_string[:50]}')

#birthday=input('Enter your birthday in format "ddmmyy":')
#if birthday in pi_string:
#    print ("Your BD is un pi!")
#else:
#    print ("Your BD is not in pi!")

with open('py_digits.txt') as testfile:
    x=testfile.read()
print (x.replace('3.14','O_O'))
