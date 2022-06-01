men={'first_name':'кирилл','last_name':'баранов','age':32,'city':'москва'}
print(f"Меня зовут {men['first_name'].title()}")
nums={
    'Ирина':7,
    'Кирилл':13,
    'Мама':5,
    }
print(f"Любимое число Мамы: {nums.get('Мам','Нет значения')}")