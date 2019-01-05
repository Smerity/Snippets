import re

my_pokemon = ['Pikachu', 'Raichu']
my_attacks = ['Thunder', 'Growl', 'Quick Attack']

pika_command = re.compile('(?P<pokemon>[A-Za-z]+),? use (?P<attack>[A-Za-z]+)')

command = input('Ash says: ')
while True:
    match = pika_command.match(command)
    if match:
        details = match.groupdict()
        if details['pokemon'] not in my_pokemon:
            print(f"You don't have a {details['pokemon']} on your team")
        else:
            if details['attack'] not in my_attacks:
                print(f"{details['pokemon']} doesn't know how to {details['attack']}")
            else:
                print(f"- {details['pokemon']} used {details['attack']}")
    else:
        print('Your Pokemon: ?!?!?!')
    command = input('Ash says: ')
