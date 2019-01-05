import re

# Imagine we're a currency conversion website!

good_currency = ['$49.50', '€12', '$16000', '£1.50']
bad_currency = ['42.0', '$20.500', '£$14.00', '$14.']

# Start with:
#############
# matching a single number
# [0123456789]
# [0-9]
# matching one or more numbers
# [0-9]+
# matching one or more numbers then a dot then one or more numbers
# [0-9]+[.][0-9]+
# matching (one or more numbers) then a single (dot or comma) then (one or more numbers)
# [0-9]+[.,][0-9]+

# EVIL LOOKING LINE
currency_pattern = re.compile('^[$£€][0-9]+([,.][0-9]{2})?$')

# re.VERBOSE allows for writing comments in the regex!
# Warning: This means that you need to escape spaces explicitly
# (where "escape" means tell it explicitly that a space is part of the pattern)
currency_pattern = re.compile('''
^                   # We want to match the start of the entry
[$£€]               # We want to start with a currency type
[0-9]+              # Then we want anything that matches 0 to 9 ([0-9] expands to [0123456789]) one or more times (+)
  (                 # Match an optional group!
    [,.]            # Match a comma or full stop
    [0-9]{2}        # Match exactly two numbers
  )?                # This group is optional
$                   # Then we want to match the end of the line
''', flags=re.VERBOSE)

print('Which currencies match?')
print('=-=-=-=')
for c in good_currency + bad_currency:
  if currency_pattern.match(c):
    print(f'+ Match on {c}')
  else:
    print(f'--- Mismatch on {c}')
