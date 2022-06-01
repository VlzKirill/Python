def city_country(city,country):
    return print(f"{city.title()}, {country.title()}")
city_country("Волжский","Россия")
city_country("Москва","Россия")
city_country("Париж","Франция")

def make_album(artist,album,tracks=None):
    artist_album = {'artist':artist,'album':album}
    if tracks:
        artist_album['tracks']=tracks
    return artist_album
x=make_album('AC/DC','Highway to Hell')
print (x)
y=make_album('Elvis Presley','Blue Suede shoes',5)
print(y)
while True:
    print('Заполните базу исполнителей и альбомов, для выхода введите "q"')
    name_p=input("Введите имя исполнителя:\n")
    if name_p == "q":
        break
    album_p=input("Введите название альбома:\n")
    if album_p == "q":
        break
    print(make_album(name_p,album_p))

