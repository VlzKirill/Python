men_0={'first_name':'кирилл','last_name':'баранов','age':32,'city':'москва',}
#print(f"Меня зовут {men_0['first_name'].title()}")
men_0['subname']='михайлович'
men_0['Семейное положение']='Женат'
for key,value in men_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")
for key,value in men_0.items():
    print (f"My {key} is {value}")
for key in men_0.keys():
    print(key)
for value in men_0.values():
    print(value)
men_1=['Кирилл','москва','Волжский']
for man in men_1:
    if man.lower() in men_0.values():
        print(f"Значение {man} уже есть в словаре")
    else:
        print (f"Значения {man} нет в словаре")


#nums={
#    'Ирина':7,
#    'Кирилл':13,
#    'Мама':5,
#    }
#print(f"Любимое число Мамы: {nums.get('Мам','Нет значения')}")