import glob
import json

fns = sorted(glob.glob('data/js/tweets/*.js'))

for fn in fns:
    data = open(fn).read()
    # Get rid of silly first line (Grailbird)
    _, data = data.split('\n', 1)
    for item in json.loads(data):
        print(json.dumps(item))
