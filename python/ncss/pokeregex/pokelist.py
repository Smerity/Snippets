import re

# Sources:
# - https://pokemondb.net/pokedex/pikachu
# - https://www.reddit.com/r/pokemon/comments/1qrnw8/i_made_a_few_plain_text_printer_friendly_pokemon/

pokemon = open('original.pokemon.txt').read()

# TODO:
# - re.sub
# - re.split

# Content 1: A friendly introduction to search using Python regex

# The many faces of Pikachu
['Pikachu', 'Piiiiiiiiiiiiikaaaaaaaaaachuuuuuuuuuuuuuu', 'Pikachuuuuuu', 'Peeeeeeekachu', 'pikachu', 'pikaCHUUUUUU']
['pikapikapikachu', 'pikapikapi', 'pika', 'pikapi']

# Multiline makes each line a separate match and allows us to use the ^ (start) and $ (end) characters to map to the start and end of each line
print('== Find any Pokemon starting with "P" that is 7 characters long')
print(re.findall(r'P......', pokemon, flags=re.MULTILINE))
# Oh no - Poliwhi was meant to be Poliwhirl!
print(re.findall(r'^P......$', pokemon, flags=re.MULTILINE))
print(re.findall(r'^P.{6}$', pokemon, flags=re.MULTILINE))
# Oh no - P.{6} would also match P123456 :S
print()

print('== Find any Pokemon starting with "Char"')
# Only match lowcase and upercase letters
print(re.findall(r'^Char[A-Za-z]+$', pokemon, flags=re.MULTILINE))
print()

print('== Find any Pokemon with "ee" in the middle')
print(re.findall('^[A-Za-z]+ee[A-Za-z]+$', pokemon, flags=re.MULTILINE))
print()

print('== Find any Pokemon ending with "saur" or "chu"')
print(re.findall(r'[A-Za-z]+saur', pokemon, flags=re.MULTILINE))
print(re.findall(r'[A-Za-z]+chu', pokemon, flags=re.MULTILINE))

# Content 2: The | Operator

print(re.findall(r'([A-Za-z]+(chu|saur))', pokemon, flags=re.MULTILINE))
print(re.findall(r'([A-Za-z]+(?:chu|saur))', pokemon, flags=re.MULTILINE))
print()

# Content 3: Groups

commands = ['Pikachu use Quick Attack', 'Pikachu use Growl', 'Raichu use Thunder', 'Pikachu, use Thunder!']
commands += ['raichu use growl']
bad_commands = ['Pikachu use Splash', 'Python use iPad']

print('== Command parsing')
# We can compile a pattern so we don't need to include it every time
pikacmd = re.compile(r'(Pikachu|Raichu),? use (Growl|Thunder|Quick Attack)!?')

for cmd in commands + bad_commands:
  print(cmd)
  match = pikacmd.match(cmd)
  if match:
    print(' + Matches with', match.groups())
  else:
    print(' - No match')
  print('---')
print()

print('== Command parsing with named groups')
pikacmd = re.compile(r'(?P<pokemon>Pikachu|Raichu),? use (?P<attack>Growl|Thunder|Quick Attack)!?', flags=re.IGNORECASE)

for cmd in commands + bad_commands:
  print(cmd)
  match = pikacmd.match(cmd)
  if match:
    print(' + Matches with', match.groupdict())
  else:
    print(' - No match')
  print('---')
print()

# Content 5: Extras

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

queries = ['At what level does Pikachu learn Nuzzle?', 'When does Pikachu learn Thunder?', 'The level pikachu learns growl?']
queries += ['When does Pikachu learn regex?', 'At what level does Python learn Java?']
pikacmd = re.compile(r'pikachu learns? ([A-Za-z]+)\?', flags=re.IGNORECASE)

for q in queries:
  print('>', q)
  match = pikacmd.search(q)
  if match:
    move = match.group(1)
    move = move.lower()
    if move in pikachu_levels:
      print('Pikachu learns {} at level {}'.format(move.title(), pikachu_levels[move]))
    else:
      print('I don\'t think Pikachu learns that :S')
  else:
    print('lolwut?')
  print()

# ? for non-greedy matching
print('PikaPikaPikachu')
