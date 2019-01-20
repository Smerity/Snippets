import struct

import fdb

fdb.api_version(600)

db = fdb.open()

db[b'hello'] = b'world'

print(db[b'hello'])

test = fdb.directory.create_or_open(db, ('test',))
dictionary = test['dict']
words = [x.rstrip() for x in open('/usr/share/dict/words').readlines()]

print(f'Loaded {len(words)}')

@fdb.transactional
def add_batch(tr, words):
    for word in words:
        #print('Adding word', word)
        tr[dictionary.pack(('words', word,))] = b''
        tr.add(dictionary.pack(('__meta__', 'count')), struct.pack('<q', 1))

def add_words(db, words, batch_size=2048):
    total = 0
    for i in range(0, len(words), batch_size):
        tmp = words[i:i + batch_size]
        print(f'Batch {i}')
        add_batch(db, tmp)
        total += len(tmp)
    assert total == len(words)

if False:
    print('Clearing words')
    db.clear_range_startswith(dictionary)

total_words = db[dictionary.pack(('__meta__', 'count'))] and struct.unpack('<q', db[dictionary.pack(('__meta__', 'count'))])[0]
if total_words is None or len(words) != total_words:
    print('Adding words')
    add_words(db, words)
else:
    print(f'Preloaded database contains {total_words} words')

#print('Naive and slow query using dictionary range')
#print(dictionary.unpack(db.get_range_startswith(dictionary)[10000].key))

for i, (k, v) in enumerate(db.get_range_startswith(dictionary, limit=100, streaming_mode=fdb.StreamingMode.iterator)):
    if i > 10: break
    _, word = dictionary.unpack(k)
    print(word)

print('Get words starting with troll')
print('Note: likely a better way of getting rid of null byte at end')
trolled = db.get_range_startswith(dictionary.pack(('words', 'troll'))[:-1])
print([dictionary.unpack(k) for k, v in trolled])