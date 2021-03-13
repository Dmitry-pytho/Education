aliens = []

for alien_number in range(0, 30):
    new_alien = {"color": "green",
                 "points": 5,
                 "speed": "slow"
                 }
    aliens.append(new_alien)

for alien in aliens[0:3]:
    if alien["color"] == "green":
        alien["color"] = "yellow"
        alien["points"] = 10
        alien["speed"] = "medium"
    # elif alien['color'] == 'yellow':
    #     alien['color'] = 'red'
    #     alien['speed'] = 'fast'
    #     alien['points'] = 15


for alien in aliens[0:5]:
    print(alien)

for alien in aliens[0:3]:
    # if alien["color"] == "green":
    #     alien["color"] = "yellow"
    #     alien["points"] = 10
    #     alien["speed"] = "medium"
    if alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15

for alien in aliens[0:5]:
    print(alien)