alien_0 = {'color':'green','points': 5 }
alien_1 = {'color':'yellow','points': 10 }
alien_2 = {'color':'red','points': 15 }
aliens = [alien_0,alien_1,alien_2]
for alien in aliens:
    print(alien)
aliens_new = {
    'color' : ['yellow','red','green'],
    'points' : [5,10,15],
    }
aliens_new['color'].append('black')
print (aliens_new['color'])