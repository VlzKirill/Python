sandwich_orders=['первый',"второй","третий","первый","четвертый","первый"]
finished_sandwiches = []
print("Первый больше нет")
while 'первый' in sandwich_orders:
    sandwich_orders.remove("первый")
while sandwich_orders:
    sandwich_orders.sort(reverse=True)
    for sandwich_order in sandwich_orders:
        print(f"Сделан {sandwich_order} сендвич")
        finished_sandwiches.append(sandwich_order)
        sandwich_orders.remove(sandwich_order)
print("Сделаны следующие сендвичи:")
for finished_sandwiche in finished_sandwiches:
    print(finished_sandwiche)
otpusk={}
opros=True
while opros:
    x=input("Хотите добавить человека, и место, где он хочет отдохнуть? (y/n)\n")
    if x=="y":
        name = input("Введите имя: ")
        place = input("Введите место отдыха: ")
        otpusk[name]=place
    elif x=="n":
        opros=False
    else:
        print("Вы ввели недопустимое значение! Попробуйте снова!\n")

print("\nРезультаты опроса:")
for name,place in otpusk.items():
    print (f"{name} хочет отдохнуть в {place}")
x=input()