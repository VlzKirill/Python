#10.3
name = input("Введите ваше имя:\n")
with open("name.txt", 'w') as save_file:
    save_file.write(name)
#10.4
while True:
    name = input("Введите ваше имя:\n Для выхода введите 'exit'")
    if name == 'exit':
        break
    else:
        message = f'Привет, {name}!'
        print (message)
        with open("message.txt", 'a') as save_file:
            save_file.write(f'{message}\n')
#10.5
while True:
    p = input ("Почему вам нравится программировать?\n")
    with open ('message2.txt', 'a') as openfile:
        openfile.write(p)