import re

pikachu_levels = {
    'growl': 1,
    'thunder shock': 1,
    'tail whip': 3,
    'quick attack': 6,
    'double kick': 9,
    'double team': 12,
    'thunder wave': 15,
    'light screen': 18,
    'thunderbolt': 21,
    'slam': 24,
    'agility': 27,
    'thunder': 30,
}

# Why does this fail?
# re.compile('At what level does Pikachu learn ([A-Za-z ])+?')
query = re.compile('At what level does Pikachu learn ([A-Za-z ])+\?', re.IGNORECASE)

while True:
    message = input('> ')
    match = query.match(message)
    if match:
        print('Match with {}'.format(match.group(0))
