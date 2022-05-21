#10.6
while True:
    try:
        x = int(input("Введите число 1"))
        y = int(input("Введите число 2"))
    except ValueError:
        print ("Вводить можно только числа")
    else:
        result = x + y
        print (result)
        break
#10.7
###########
testfiles = ['cats.txt','dogs.txt']
#10.8- 9
for testfile in testfiles:
    try:
        with open(testfile, 'r') as file:
            workfile=file.readlines()
    except FileNotFoundError:
        print(f"Файл {testfile} не найден!")
        pass
    else:
        print (workfile)
#10.9