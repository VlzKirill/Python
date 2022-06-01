nachinki=["пепперони", "сыр", "грибы"]
message="Введите доп. начинку. "
message+="\nЧтобы показать доступные начинки, нажмите '1'"
message+="\nДля выхода наберите 'quit'"
mes=""
while True:
    mes=input(message)
    if mes=='quit':
        break
    elif mes=='1':
            for nachinka in nachinki:
                print(nachinka)
    print(f"{mes} добавлена как начинка")