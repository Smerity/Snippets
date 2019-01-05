import re

good_reminds = ['Remind me in 5 minutes', 'Remind me in 1 days', 'Remind me in 4 hours', 'Remind me in 42 minutes']
bad_reminds = ['Remind me in 4 parsecs', 'Remind me in a day']

for remind in good_reminds + bad_reminds:
  match = re.match('Remind me in [0-9]+ (second|minute|hour|day)', remind)
  if match:
    print(match)
    print(match.groups())
  else:
    print(f'- Reminder "{remind}" was not matched by the regular expression')
