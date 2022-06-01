favorite_places = {'mary':['London','Paris','Moscow'],
    'daniel':['Volgograd','Lissabon']}
for x,y in favorite_places.items():
    print (f"\nFavorite place of {x.title()} is:")
    for y1 in y:
        print (y1)
print()
cities = {'Moscow':{'country':'Russia','population':'142_000_000'},
    'Paris':{'country':'France','population':'80_000_000'},
    'London':{'country':'England','population':'70_000_000'},
    }
for city,info in cities.items():
    print(f"\n{city}:")
    for key,value in info.items():
        print(f"{key} is {value}")