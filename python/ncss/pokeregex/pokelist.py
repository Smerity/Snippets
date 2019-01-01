import re

# Sources:
# - https://pokemondb.net/pokedex/pikachu
# - https://www.reddit.com/r/pokemon/comments/1qrnw8/i_made_a_few_plain_text_printer_friendly_pokemon/

pokemon = open('original.pokemon.txt').read()

# TODO: Content 1: A friendly introduction to search using Python regex

print('== Find any Pokemon starting with "P" that is 7 characters long')
print(re.findall(r'P......', pokemon, flags=re.MULTILINE))
# Oh no - Poliwhi was meant to be Poliwhirl!
print(re.findall(r'^P......$', pokemon, flags=re.MULTILINE))
print(re.findall(r'^P.{6}$', pokemon, flags=re.MULTILINE))
print()

print('== Find any Pokemon starting with "Char"')
print(re.findall(r'Char[A-Za-z]+', pokemon))
print()

print('== Find any Pokemon ending with "saur" or "chu"')
print(re.findall(r'[A-Za-z]+saur', pokemon))
print(re.findall(r'[A-Za-z]+chu', pokemon))
print(re.findall(r'([A-Za-z]+(chu|saur))', pokemon))
print(re.findall(r'([A-Za-z]+(?:chu|saur))', pokemon))
print()

# Content 2: The | Operator

# Content 3: Groups

commands = ['Pikachu use Quick Attack', 'Pikachu use Growl', 'Raichu use Thunder']
commands += ['raichu use growl']
bad_commands = ['Pikachu use Splash', 'Python use iPad']

print('== Command parsing')
pikacmd = re.compile(r'(Pikachu|Raichu) use (Growl|Thunder|Quick Attack)')
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
pikacmd = re.compile(r'(?P<pokemon>Pikachu|Raichu) use (?P<attack>Growl|Thunder|Quick Attack)', flags=re.IGNORECASE)

for cmd in commands + bad_commands:
  print(cmd)
  match = pikacmd.match(cmd)
  if match:
    print(' + Matches with', match.groupdict())
  else:
    print(' - No match')
  print('---')
print()

# Content 4: The ? Operator

# Content 5: Extras

print('At what level does Pikachu learn Nuzzle?')

print('PikaPikaPikachu')
