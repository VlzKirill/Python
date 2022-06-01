nachinki=["пепперони", "сыр", "грибы"]
message="\nВведите доп. начинку. "
message+="\nЧтобы показать доступные начинки, нажмите '1'"
message+="\nЧтобы показать добавленные начинки, нажмите '2'"
message+="\nДля выхода наберите 'quit'"
message+="\n"
mes=""
dob_nachinki=[]
while True:
    mes=input(message)
    if mes=='quit':
        break
    elif mes=='1':
        for nachinka in nachinki:
            print(nachinka)
    elif mes=='2':
        if dob_nachinki:
            print('\nСписок добавленных начинок:')
            for dob_nachinka in dob_nachinki:
                print(dob_nachinka)
        else:
            print("Нет добавленных начинок")
    elif mes in nachinki:
        print(f"Добавлена новая начинка: {mes}")
        for nachinka in nachinki:
            if mes==nachinka:
                dob_nachinki.append(nachinka)
                nachinki.remove(nachinka)
    elif mes in dob_nachinki:
        print(f"Начинка {mes} уже добавлена")
    else:
        print(f"Начинки {mes} нет в списке доступных начинок")
