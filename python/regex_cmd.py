# I can never ever remember this off of the top of my head
# I guess I shouldn't be surprised considering it's regex...
import re

r = re.compile("{([^,]*),([^}]*)}")

# This replaces {<TXT>,<NUM>} with <TXT> * <NUM>
# Lambda as lazy :)
def regex_cmd(s):
  return r.sub(lambda m: m.group(1) * int(m.group(2)), s)

print regex_cmd("I want a big {house,1} with a millions {bon,2}s{.,3}")
