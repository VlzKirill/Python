users=['admin','user1','user2','user3','user4']
for user in users:
    if user=="admin":
        print(f'Привет, {user}, не хотите посмотреть отчет?')
    else:
        print(f'Привет, {user}')